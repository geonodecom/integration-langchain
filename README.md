![Geonode for LangChain: Web Scraping Tools for AI Agents](assets/banner.svg)

# Geonode for LangChain: Web Scraping Tools for AI Agents

Give your LangChain agents web search and page content for research and retrieval workflows. Extract pages, crawl sites, discover URLs and run batches. Use the returned content in your own research and RAG pipelines, with tools to retrieve or wait for background jobs.

**[Try Geonode for free](https://app.geonode.com/sign-up)**

[Integrations page](https://geonode.com/integrations) · [Geonode API docs](https://docs.geonode.com/docs/scraper-api) · [LangChain setup guide](https://docs.geonode.com/docs/scraper-api/guides/sdks/langchain) · [View package on PyPI](https://pypi.org/project/geonode-scraper-langchain/) · [View source on GitHub](https://github.com/geonodecom/integration-langchain) · [Complete guide](docs/guide.md)

<!-- BEGIN README NAV -->
[Quick start](#quick-start) · [Available operations](#available-operations) · [Example: a research workflow in LangChain](#example-a-research-workflow-in-langchain) · [Setup questions](#setup-questions)
<!-- END README NAV -->

## Workflow ideas

- **Research with source material.** Let an agent search for relevant pages and extract their content before composing an answer with source URLs.
- **Prepare a retrieval corpus.** Map a site, select relevant URLs and extract Markdown for your own indexing pipeline.

## Quick start

Requires Python 3.10 or newer and a Geonode API key from the [dashboard](https://app.geonode.com/). The direct-tool example works without a language model.

```sh
pip install geonode-scraper-langchain
export GEONODE_SCRAPER_API_KEY="your-api-key"
```

```python
import os

from geonode_scraper_langchain import build_langchain_tools
from geonode_scraper_tools_core import ScraperToolSettings

settings = ScraperToolSettings(
    host="https://scraper.geonode.io",
    api_key=os.environ["GEONODE_SCRAPER_API_KEY"],
)
tools = build_langchain_tools(settings=settings, operations=["extract"])
extract = next(tool for tool in tools if tool.name == "scraper_extract_content")
outcome = extract.invoke({"url": "https://example.com", "formats": ["markdown"]})

if outcome["ok"]:
    print(outcome["result"]["data"]["markdown"])
else:
    print(outcome["error"]["status"], outcome["error"]["message"])
```

API calls use your Geonode plan. Successful tools return `ok`, `operation`, `attempts` and `result`; API failures return a structured `error` with status, message and retryability. Validation or framework errors may still raise before an API request.

## Use with an agent

Install your model provider's integration and set its credentials separately. Set `LANGCHAIN_MODEL` to a model identifier supported by your installed LangChain version. Install `langchain` in addition to this package; the package itself depends only on `langchain-core`.

Continue from the configured `tools` above:

```python
from langchain.agents import create_agent

agent = create_agent(os.environ["LANGCHAIN_MODEL"], tools=tools)
result = agent.invoke({"messages": [{"role": "user", "content": "Summarize https://example.com"}]})
print(result["messages"][-1].content)
```

The model chooses tool calls. Restrict the available operations to the tasks your agent needs:

```python
tools = build_langchain_tools(
    settings=settings,
    operations=["extract", "map_urls", "search"],
)
```

## Available operations

| Task | Operations |
| --- | --- |
| Extract pages | `extract`, `get_job_result`, `wait_for_job`, `list_jobs` |
| Batch extraction | `create_batch`, `get_batch_status`, `wait_for_batch`, `list_batch_jobs` |
| Crawl websites | `create_crawl`, `get_crawl_status`, `wait_for_crawl`, `list_crawl_jobs` |
| Map website URLs | `map_urls`, `list_map_jobs`, `get_map_job` |
| Search the web | `search`, `list_search_jobs`, `get_search_job` |
| Account and service | `get_statistics`, `get_concurrency_usage`, `health_check` |

The [complete guide](docs/guide.md) lists each tool ID, settings, polling and response handling. The shared [`geonode-scraper-tools-core`](https://pypi.org/project/geonode-scraper-tools-core/) runtime is installed automatically. This package integrates directly with LangChain; it does not start an MCP server.

<!-- BEGIN SHARED WORKFLOW GUIDE -->
## Understand the tool result

The toolkit wraps successful API results with ok, operation, attempts and result. For synchronous Markdown extraction, check ok before reading result.data.markdown. API failures return an error with status, code, message and retryable; argument-validation or framework errors can raise before that envelope is returned.

The quick start calls a tool directly, without a model. Once that succeeds, give the selected tools to your agent and configure its model provider separately. The Geonode key and model-provider key are different credentials.

## Example: a research workflow in LangChain

1. Choose only the extract, map_urls and search operations for a focused research task.
2. Ask the agent to discover relevant URLs, select a small set, and extract those pages as Markdown.
3. Require it to inspect tool errors and retain the source URL for every page it uses.
4. Pass the extracted content to the model for analysis, then save the answer with its sources in your own application.
5. Use explicit page limits and a separate completion check if the task needs a crawl or batch.

**Expected result:** The tools return web content and job results. The model performs the reasoning and summarization; these toolkits do not supply a vector database, a model subscription or a ready-made research agent.

## Setup questions

Why is the agent not calling a tool? First run the direct-tool example, then check that your agent receives the selected tools and that its model supports tool calling. Installing the package alone does not configure an agent.

Why did a long job time out? Request timeouts and wait-tool polling timeouts are separate. Preserve the job ID and retrieve its state before retrying a submission.

Do I need agent tools core separately? The framework package installs the shared runtime as a dependency. Use it directly only when building your own adapter.

Is this MCP? These are native framework tools. Use the separate Geonode MCP connection for an MCP-compatible assistant.

These recipes describe source-supported workflows. They have not been run as authenticated end-to-end examples in this review.
<!-- END SHARED WORKFLOW GUIDE -->

## Development and support

See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and [release migration](docs/release-migration.md) for the current publishing boundary. Publishing remains in the existing SDK monorepo until a coordinated cutover.

For API or account questions, [contact Geonode](https://geonode.com/contact). For security issues, follow [SECURITY.md](SECURITY.md). Licensed under [MIT](LICENSE).

**[Try Geonode for free](https://app.geonode.com/sign-up)**
