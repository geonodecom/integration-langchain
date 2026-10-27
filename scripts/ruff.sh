#!/usr/bin/env bash
set -euo pipefail
mode="${1:-check}"
if [[ $# -gt 0 ]]; then shift; fi
pkg_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$pkg_dir"
if [[ $# -eq 0 ]]; then set -- geonode_scraper_langchain tests; fi
if command -v uv >/dev/null 2>&1; then
  ruff_cmd=(uv run --extra dev ruff)
else
  ruff_cmd=(python -m ruff)
fi
case "$mode" in
  check|format) "${ruff_cmd[@]}" "$mode" "$@" ;;
  *) printf 'Usage: %s <check|format> [paths ...]\n' "$0" >&2; exit 2 ;;
esac
