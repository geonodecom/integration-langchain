# Contributing

Use Python 3.11 for the tested development environment. Runtime compatibility is declared in `pyproject.toml`.

```sh
uv sync --extra dev
./scripts/ruff.sh check
./scripts/test.sh
uv build
```

Without uv, create and activate a virtual environment, install `pip install -e ".[dev]" build`, then use `python -m ruff check .`, `python -m pytest` and `python -m build`.

Branch from `main`, keep each change focused, and add a changelog entry under `Unreleased`. Preserve package names, import paths and public tool IDs. Do not bump a version or upload a package as part of a normal change.

Tests use mocked services and the published `geonode-scraper-tools-core` dependency. No sibling checkout or live API credential is needed. For a deliberate integration test, supply credentials only through your local environment and describe any API usage separately from unit-test results.

Report package bugs with the package version, minimal reproduction and sanitized output. For API/account help, [contact Geonode](https://geonode.com/contact). Report vulnerabilities through [SECURITY.md](SECURITY.md), never in an issue.

Maintainers publish releases with the `Publish` workflow in GitHub Actions. Contributions use the [MIT license](LICENSE).
