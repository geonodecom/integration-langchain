# Geonode Scraper tools for LangChain

[Integrations page](https://geonode.com/integrations) · [Geonode API docs](https://docs.geonode.com/docs/scraper-api) · [GitHub source](https://github.com/geonodecom/integration-langchain) · [LangChain setup guide](https://docs.geonode.com/docs/scraper-api/guides/sdks/langchain) · [Published package](https://pypi.org/project/geonode-scraper-langchain/) · [Repository overview](../README.md)

**[Try Geonode for free](https://app.geonode.com/sign-up)**

21 LangChain tools that let an agent read web pages through the [Geonode Scraper API](https://geonode.com/products/scraper-api): extract a page as Markdown or HTML, run batches and crawls, map a site's URLs, search the web and check usage. Package: [`geonode-scraper-langchain` on PyPI](https://pypi.org/project/geonode-scraper-langchain/).

## Before you start

- Python 3.10 or newer.
- A Geonode API key. Sign in to the [Geonode dashboard](https://app.geonode.com/), open **API Keys**, and create a key or copy an existing one.
- A chat model for your agent, from any provider LangChain supports.

## Install

```sh
pip install geonode-scraper-langchain
```

This installs `langchain-core` and the shared [`geonode-scraper-tools-core`](https://pypi.org/project/geonode-scraper-tools-core/). For the agent example below, also install `langchain` and your model provider's package, for example `pip install langchain langchain-anthropic`.

## Configure

Set `GEONODE_SCRAPER_API_KEY` to your Geonode key. For the agent example, set `LANGCHAIN_MODEL` to a model supported by your installed framework and configure its provider credentials separately. The direct-tool example does not require a model.

```python
import os

from geonode_scraper_langchain import build_langchain_tools
from geonode_scraper_tools_core import ScraperToolSettings

settings = ScraperToolSettings(
    host="https://scraper.geonode.io",
    api_key=os.environ["GEONODE_SCRAPER_API_KEY"],
)
tools = build_langchain_tools(settings=settings)
```

`host` and `api_key` are required. The other settings have defaults:

| Setting | Default | What it does |
|---|---|---|
| `request_timeout` | none | Seconds to wait for each HTTP response. |
| `max_retries` | `0` | Extra attempts after a failed request. |
| `retry_backoff_seconds` | `1.0` | Pause before the first retry. |
| `poll_interval_seconds` | `3.0` | How often the `wait_for_*` tools check a job. |
| `poll_timeout_seconds` | `60.0` | How long the `wait_for_*` tools wait before giving up. |
| `verify_ssl` | `True` | Check TLS certificates. |

## Use the tools in an agent

```python
from langchain.agents import create_agent

agent = create_agent(os.environ["LANGCHAIN_MODEL"], tools=tools)
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What does https://example.com say? Answer in one sentence."}]}
)
print(result["messages"][-1].content)
```

Any LangChain chat model works in place of the model name. The agent chooses which tools to call. For this task, `scraper_extract_content` provides the page Markdown; the exact tool calls depend on your model.

## Call a tool directly

Every tool is a regular LangChain tool, so you can call it without an agent, for example in a test:

```python
extract = next(t for t in tools if t.name == "scraper_extract_content")
outcome = extract.invoke({"url": "https://example.com", "formats": ["markdown"]})
if outcome["ok"]:
    print(outcome["result"]["data"]["markdown"])
else:
    print(outcome["error"]["status"], outcome["error"]["message"])
```

## What a tool returns

Tools don't raise on API errors. They return a dict, so the agent can read what went wrong and decide what to do:

- On success: `{"ok": true, "operation": "...", "attempts": 1, "result": {...}}`.
- On failure: `{"ok": false, "operation": "...", "attempts": 1, "error": {"status": 429, "code": "...", "message": "...", "retryable": true, ...}}`.

`status` is the API's HTTP status; the [Python SDK page](https://pypi.org/project/geonode-scraper-sdk/) lists what each one means. `retryable` says whether trying again can help.

## Pick only the tools you need

Fewer tools make it easier for a model to choose. Pass the operation names you want:

```python
tools = build_langchain_tools(settings=settings, operations=["extract", "map_urls", "search"])
```

| Operation | Tool | What it does |
|---|---|---|
| `extract` | `scraper_extract_content` | Extract one URL as Markdown or HTML, now or as a background job. |
| `get_job_result` | `scraper_get_job_result` | Get the state or result of a background extraction. |
| `wait_for_job` | `scraper_wait_for_job` | Wait until a background extraction finishes. |
| `list_jobs` | `scraper_list_jobs` | List earlier extractions. |
| `create_batch` | `scraper_create_batch` | Start one job for many URLs. |
| `get_batch_status` | `scraper_get_batch_status` | Get a batch's progress and results so far. |
| `wait_for_batch` | `scraper_wait_for_batch` | Wait until a batch finishes. |
| `list_batch_jobs` | `scraper_list_batch_jobs` | List earlier batches. |
| `create_crawl` | `scraper_create_crawl` | Start a crawl from one URL. |
| `get_crawl_status` | `scraper_get_crawl_status` | Get a crawl's progress and pages so far. |
| `wait_for_crawl` | `scraper_wait_for_crawl` | Wait until a crawl finishes. |
| `list_crawl_jobs` | `scraper_list_crawl_jobs` | List earlier crawls. |
| `map_urls` | `scraper_map_urls` | Find the URLs under a site from its sitemap and links. |
| `list_map_jobs` | `scraper_list_map_jobs` | List earlier map runs. |
| `get_map_job` | `scraper_get_map_job` | Get one map run with its URLs. |
| `search` | `scraper_search` | Search the web and return ranked results. |
| `list_search_jobs` | `scraper_list_search_jobs` | List earlier searches. |
| `get_search_job` | `scraper_get_search_job` | Get one search with its results. |
| `get_statistics` | `scraper_get_statistics` | Usage statistics for a period. |
| `get_concurrency_usage` | `scraper_get_concurrency_usage` | Concurrent requests in use against the plan limit. |
| `health_check` | `scraper_check_health` | Check that the API is up. |

## Versions and support

- The latest version is on [PyPI](https://pypi.org/project/geonode-scraper-langchain/). The same tools are available for [CrewAI](https://pypi.org/project/geonode-scraper-crewai/).
- Requests send `User-Agent: geonode-langchain/<version>`, which helps support see which version you use.
- Questions or problems: [contact Geonode](https://geonode.com/contact).
