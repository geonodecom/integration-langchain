# LangChain: workflow recipes and output guide

[Repository overview](../README.md) · [Geonode documentation](https://docs.geonode.com/docs/scraper-api/guides/sdks/langchain)

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

Source-reviewed recipes; authenticated workflow execution has not been tested in this review.
