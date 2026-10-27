#!/usr/bin/env bash
set -euo pipefail
pkg_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$pkg_dir"
if command -v uv >/dev/null 2>&1; then
  uv run --extra dev pytest tests "$@"
else
  python -m pytest tests "$@"
fi
