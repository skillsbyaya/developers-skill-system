#!/bin/sh
set -eu

usage() {
  echo "Usage: $0 [--link] [claude]" >&2
  echo "  --link  symlink to this clone instead of copying, so edits here are live at once" >&2
  exit 2
}

link=false
if [ "${1:-}" = --link ]; then
  link=true
  shift
fi

[ "${1:-claude}" = claude ] || usage

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd)
install_home=${DEVELOPERS_SKILL_HOME:-$HOME}
target=$install_home/.claude/skills
manifest=$target/.developers-skill-system.manifest
next_manifest=$target/.developers-skill-system.manifest.next

place() {
  rm -rf -- "$2"
  if [ "$link" = true ]; then
    ln -s "$1" "$2"
  else
    cp -R "$1" "$2"
  fi
}

mkdir -p "$target"
: > "$next_manifest"

for source in "$repo_root"/skills/*; do
  [ -d "$source" ] || continue
  name=$(basename "$source")
  place "$source" "$target/$name"
  printf '%s\n' "$name" >> "$next_manifest"
done

if [ -f "$manifest" ]; then
  while IFS= read -r old_name; do
    case "$old_name" in
      ''|*[!a-z0-9-]*) continue ;;
    esac
    if ! grep -qx "$old_name" "$next_manifest"; then
      rm -rf -- "$target/$old_name"
    fi
  done < "$manifest"
fi

sort -u "$next_manifest" > "$manifest"
rm -f -- "$next_manifest"

agents=$install_home/.claude/agents
mkdir -p "$agents"
for source in "$repo_root"/subagents/claude-code/*.md; do
  [ -f "$source" ] || continue
  place "$source" "$agents/$(basename "$source")"
done

if [ "$link" = true ]; then
  echo "Linked skills in $target to $repo_root"
else
  echo "Installed skills in $target"
fi
