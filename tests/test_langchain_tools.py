from __future__ import annotations

from geonode_scraper_langchain import build_langchain_tools


class StubService:
    def extract(self, **kwargs):
        return {"ok": True, "operation": "extract", "result": kwargs}

    def get_job_result(self, **kwargs):
        return {"ok": True, "operation": "get_job_result", "result": kwargs}

    def wait_for_job(self, **kwargs):
        return {"ok": True, "operation": "wait_for_job", "result": kwargs}

    def list_jobs(self, **kwargs):
        return {"ok": True, "operation": "list_jobs", "result": kwargs}

    def get_statistics(self, **kwargs):
        return {"ok": True, "operation": "get_statistics", "result": kwargs}

    def health_check(self, **kwargs):
        return {"ok": True, "operation": "health_check", "result": kwargs}

    def create_batch(self, **kwargs):
        return {"ok": True, "operation": "create_batch", "result": kwargs}

    def get_batch_status(self, **kwargs):
        return {"ok": True, "operation": "get_batch_status", "result": kwargs}

    def wait_for_batch(self, **kwargs):
        return {"ok": True, "operation": "wait_for_batch", "result": kwargs}

    def create_crawl(self, **kwargs):
        return {"ok": True, "operation": "create_crawl", "result": kwargs}

    def get_crawl_status(self, **kwargs):
        return {"ok": True, "operation": "get_crawl_status", "result": kwargs}

    def wait_for_crawl(self, **kwargs):
        return {"ok": True, "operation": "wait_for_crawl", "result": kwargs}

    def map_urls(self, **kwargs):
        return {"ok": True, "operation": "map_urls", "result": kwargs}

    def list_batch_jobs(self, **kwargs):
        return {"ok": True, "operation": "list_batch_jobs", "result": kwargs}

    def list_crawl_jobs(self, **kwargs):
        return {"ok": True, "operation": "list_crawl_jobs", "result": kwargs}

    def list_map_jobs(self, **kwargs):
        return {"ok": True, "operation": "list_map_jobs", "result": kwargs}

    def get_map_job(self, **kwargs):
        return {"ok": True, "operation": "get_map_job", "result": kwargs}

    def search(self, **kwargs):
        return {"ok": True, "operation": "search", "result": kwargs}

    def list_search_jobs(self, **kwargs):
        return {"ok": True, "operation": "list_search_jobs", "result": kwargs}

    def get_search_job(self, **kwargs):
        return {"ok": True, "operation": "get_search_job", "result": kwargs}

    def get_concurrency_usage(self, **kwargs):
        return {"ok": True, "operation": "get_concurrency_usage", "result": kwargs}


def test_build_langchain_tools_exposes_expected_names():
    pytest = __import__("pytest")
    pytest.importorskip("langchain_core.tools")

    tools = build_langchain_tools(service=StubService())

    assert [tool.name for tool in tools] == [
        "scraper_extract_content",
        "scraper_get_job_result",
        "scraper_wait_for_job",
        "scraper_list_jobs",
        "scraper_get_statistics",
        "scraper_check_health",
        "scraper_create_batch",
        "scraper_get_batch_status",
        "scraper_wait_for_batch",
        "scraper_create_crawl",
        "scraper_get_crawl_status",
        "scraper_wait_for_crawl",
        "scraper_map_urls",
        "scraper_list_batch_jobs",
        "scraper_list_crawl_jobs",
        "scraper_list_map_jobs",
        "scraper_get_map_job",
        "scraper_search",
        "scraper_list_search_jobs",
        "scraper_get_search_job",
        "scraper_get_concurrency_usage",
    ]
    assert len(tools) == 21


def test_langchain_tool_invocation_returns_structured_output():
    pytest = __import__("pytest")
    pytest.importorskip("langchain_core.tools")

    tools = build_langchain_tools(service=StubService(), operations=["extract"])
    result = tools[0].invoke({"url": "https://example.com"})

    assert result["ok"] is True
    assert result["operation"] == "extract"
    assert result["result"]["url"] == "https://example.com"


def test_langchain_wait_for_job_tool_is_selectable():
    pytest = __import__("pytest")
    pytest.importorskip("langchain_core.tools")

    tools = build_langchain_tools(service=StubService(), operations=["wait_for_job"])
    result = tools[0].invoke({"job_id": "test-job-uuid"})

    assert result["ok"] is True
    assert result["operation"] == "wait_for_job"
    assert result["result"]["job_id"] == "test-job-uuid"


def test_langchain_map_urls_tool_is_selectable():
    pytest = __import__("pytest")
    pytest.importorskip("langchain_core.tools")

    tools = build_langchain_tools(service=StubService(), operations=["map_urls"])
    result = tools[0].invoke({"url": "https://example.com"})

    assert result["ok"] is True
    assert result["operation"] == "map_urls"
    assert result["result"]["url"] == "https://example.com"


def test_langchain_search_tool_is_selectable():
    pytest = __import__("pytest")
    pytest.importorskip("langchain_core.tools")

    tools = build_langchain_tools(service=StubService(), operations=["search"])
    result = tools[0].invoke({"query": "geonode scraper api"})

    assert result["ok"] is True
    assert result["operation"] == "search"
    assert result["result"]["query"] == "geonode scraper api"


def test_langchain_create_batch_tool_is_selectable():
    pytest = __import__("pytest")
    pytest.importorskip("langchain_core.tools")

    tools = build_langchain_tools(service=StubService(), operations=["create_batch"])
    result = tools[0].invoke({"urls": ["https://a.com", "https://b.com"]})

    assert result["ok"] is True
    assert result["operation"] == "create_batch"
    assert result["result"]["urls"] == ["https://a.com", "https://b.com"]
