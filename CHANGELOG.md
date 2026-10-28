# Changelog

All notable changes to the LangChain Tools package will be documented in this file.

The format is inspired by Keep a Changelog.

## [Unreleased]

## [0.4.3] - 2026-10-28

- Removed the internal repository preparation notes and links to the old monorepo.

- Docs links point to the package's page at https://docs.geonode.com/docs/scraper-api/guides/sdks/langchain.

- README rewritten so it can be published as the package page on docs.geonode.com: setup with the real API host, an agent example, calling a tool directly, what a tool returns, and the full tool list. The old example set a placeholder `host`.

## [0.4.2] - 2026-10-21

- The package page links to geonode.com, the Scraper API docs and sign-up.
- README: a sign-up link near the top.

## [0.4.1] - 2026-10-19

- Tools built from settings name themselves in every request: `User-Agent: geonode-langchain/<version> geonode-agent-tools/<version> geonode-python-sdk/<version>`. Tools built from a `service` you pass in keep that service's User-Agent.
- Bumped `geonode-scraper-tools-core` dependency to `>=0.5.0`.

## [0.4.0] - 2026-07-15

- Exposes 4 new tools via updated `geonode-scraper-tools-core`: `scraper_search`, `scraper_list_search_jobs`, `scraper_get_search_job`, `scraper_get_concurrency_usage` (21 tools total).
- The `scraper_map_urls` tool now defaults `include_subdomains` to `False` (previously `True`), matching the API's new default discovery scope.
- Bumped `geonode-scraper-tools-core` dependency to `>=0.4.0`.

## [0.3.0] - 2026-06-11

- Exposes 4 new tools via updated `geonode-scraper-tools-core`: `scraper_list_batch_jobs`, `scraper_list_crawl_jobs`, `scraper_list_map_jobs`, `scraper_get_map_job` (17 tools total).
- The `extract` tool no longer accepts `extract_links` (the field was removed from the API).
- Bumped `geonode-scraper-tools-core` dependency to `>=0.3.0`.

## [0.2.0] - 2026-06-03

- Exposes 7 new tools via updated `geonode-scraper-tools-core`: `scraper_create_batch`, `scraper_get_batch_status`, `scraper_wait_for_batch`, `scraper_create_crawl`, `scraper_get_crawl_status`, `scraper_wait_for_crawl`, `scraper_map_urls`.
- Bumped `geonode-scraper-tools-core` dependency to `>=0.2.0`.

## [0.1.0] - 2026-04-09

- Initial release with LangChain toolkit wrapping extraction, job management, statistics, and health check operations.
