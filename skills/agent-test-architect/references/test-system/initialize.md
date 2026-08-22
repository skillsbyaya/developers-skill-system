# Initialize

Establish the smallest useful missing layer without disturbing working infrastructure.

1. Identify the missing unit/component, integration, API, browser/end-to-end, or language-native layer.
2. Prefer an installed framework and current repository convention. If a new dependency is needed, verify the supported choice for the detected stack from official sources.
3. Present the proposed framework, layer, dependencies, config or scripts, location, representative test, and environment needs. Obtain confirmation before adding or replacing dependencies or creating a competing framework.
4. Use the repository's package manager and pinned runtime. Do not create competing lockfiles or version files.
5. Add only the required config, directories, and local commands. Add one representative passing test against real project behaviour when such behaviour exists. If the project has no implemented behaviour yet, add no placeholder assertion; let the first ATDD scaffold prove discovery and controlled red execution after setup.
6. Verify installation, command execution, discovery, a meaningful passing test when available, relevant existing tests, configuration, environment examples, generated artifacts, and ignore rules.

Update existing concise developer or testing instructions when the commands would otherwise be undiscoverable. CI wiring is a separately selected CI quality-pipeline workflow; do not silently add it during framework setup.

If the environment blocks a real passing test, stop with the minimal configuration that can be verified and name the exact unverified step. Do not substitute a meaningless assertion.
