# Preparation verification

Checked locally on 2026-10-21 using Python 3.11.16 on macOS arm64.

- Isolated dependency installation with `uv sync --extra dev` succeeded. The checked resolution is saved in `uv.lock`; shared dependencies came from PyPI (`geonode-scraper-sdk` 0.6.1 and `geonode-scraper-tools-core` 0.5.1), not sibling folders.
- `ruff check .` passed. Standalone import classification required test import formatting only.
- `pytest -q`: **8 passed**. Tests mock HTTP/service behavior; no live scraping or model-provider calls were made.
- `uv build` produced both source distribution and wheel at the existing package version. Build outputs stay ignored and were not published.
- Python snippets in README and the complete guide passed syntax parsing. Model-agent examples need separately configured provider packages and credentials and were not executed.
- Runtime source files were compared byte for byte with the original subtree and are unchanged.
- A bounded credential-pattern scan of tracked files and 36 historical blobs found no matches for private-key headers, GitHub/Slack tokens, AWS access IDs or long literal credential assignments. This is not a comprehensive security audit.

Repository release authority remains unchanged; see [release migration](release-migration.md). Other Python/platform combinations and authenticated production API behavior were not tested in this preparation.
