import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from analyze_sources import build_analysis, resolve_inputs


class AnalyzeSourcesTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "brief.md").write_text("# Brief\nSmall source")
        (self.root / "notes.txt").write_text("Notes")
        (self.root / "table.csv").write_text("a,b\n1,2\n")
        (self.root / "image.png").write_bytes(b"not text")
        nested = self.root / "nested"
        nested.mkdir()
        (nested / "decision.yaml").write_text("decision: keep")
        skipped = self.root / "node_modules"
        skipped.mkdir()
        (skipped / "junk.md").write_text("skip")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_resolve_folder_filters_and_recurses(self):
        names = {path.name for path in resolve_inputs([str(self.root)])}
        self.assertEqual(names, {"brief.md", "notes.txt", "table.csv", "decision.yaml"})

    def test_resolve_deduplicates(self):
        path = str(self.root / "brief.md")
        self.assertEqual(len(resolve_inputs([path, path])), 1)

    def test_small_set_stays_inline(self):
        result = build_analysis([str(self.root / "brief.md")])
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["routing"]["recommendation"], "inline")
        self.assertEqual(result["split_prediction"]["prediction"], "unlikely")

    def test_large_set_recommends_partition(self):
        for index in range(4):
            (self.root / f"doc-{index}.md").write_text("x" * 100)
        result = build_analysis([str(self.root)])
        self.assertEqual(result["routing"]["recommendation"], "partition")

    def test_glob_resolves_supported_files(self):
        paths = resolve_inputs([str(self.root / "*.md")])
        self.assertEqual([path.name for path in paths], ["brief.md"])

    def test_large_source_suggests_considering_split(self):
        large = self.root / "large.md"
        large.write_text("x" * 70_000)
        result = build_analysis([str(large)])
        self.assertEqual(result["split_prediction"]["prediction"], "consider")

    def test_empty_input_reports_error(self):
        result = build_analysis(["/definitely/not/here"])
        self.assertEqual(result["status"], "error")

    def test_cli_emits_json(self):
        script = Path(__file__).parent.parent / "analyze_sources.py"
        completed = subprocess.run(
            [sys.executable, str(script), str(self.root / "brief.md")],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(json.loads(completed.stdout)["status"], "ok")


if __name__ == "__main__":
    unittest.main()
