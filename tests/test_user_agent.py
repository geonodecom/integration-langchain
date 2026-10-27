from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
import urllib3
from geonode_scraper_tools_core import ScraperToolSettings

from geonode_scraper_langchain import ScraperLangChainToolkit, __version__, build_langchain_tools

SETTINGS = ScraperToolSettings(host="http://api.mock.local", api_key="test-mock-api-key")
HEALTH = {"version": "0.1.0", "service": "scraper-api", "timestamp": "2026-01-01T00:00:00Z", "status": "ok"}


def _health_response() -> MagicMock:
    response = MagicMock(status=200, reason="OK", data=json.dumps(HEALTH).encode())
    response.headers = {"content-type": "application/json"}
    return response


@pytest.mark.parametrize(
    "build_tools",
    [
        lambda: build_langchain_tools(settings=SETTINGS, operations=["health_check"]),
        lambda: ScraperLangChainToolkit.from_settings(SETTINGS).get_tools(["health_check"]),
    ],
    ids=["build_langchain_tools", "from_settings"],
)
def test_requests_name_langchain_first(build_tools):
    # The API labels a request by the first User-Agent token (scraper-api#674).
    pytest.importorskip("langchain_core.tools")
    (tool,) = build_tools()

    with patch.object(urllib3.PoolManager, "request", return_value=_health_response()) as request:
        assert tool.invoke({})["ok"] is True

    assert request.call_args.kwargs["headers"]["User-Agent"].split()[0] == f"geonode-langchain/{__version__}"
