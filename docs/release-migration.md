# Release migration

**Package publishing remains in `geonodecom/scraper-api-sdks`.** This repository is a prepared source split, not a second release authority. The published package remains [`geonode-scraper-langchain`](https://pypi.org/project/geonode-scraper-langchain/), with its existing import paths and tool IDs.

`geonode-scraper-tools-core` remains a dependency installed from PyPI; it is not vendored and no new core repository is required. This preparation adds no registry token, trusted publisher, release workflow, or version bump.

Before moving releases, maintainers must reconcile changes with the monorepo, designate one publishing source, configure the corresponding PyPI trusted publisher, test build artifacts, document the cutover and retire the old workflow for this package. Coordinate updates to source/documentation URLs with that cutover. Do not publish the same version from both repositories.

Development commands and unit tests validate local packaging and mocked behavior. They do not prove authenticated scraping or production release delivery.

## Signup offer release check

The README uses the product-owner-approved launch copy, “Sign up to get 10,000 free credits” (21 October 2026). Before public release, verify that the live signup flow and account credit allocation match this offer. This copy update does not configure billing or issue credits.

## Cross-link deployment handoff

The README and package homepage link to the live [integrations hub](https://geonode.com/integrations). The intended detail destination is `https://geonode.com/integrations/langchain`; it is a deployment target, not a verified public page. After that detail page is deployed and checked, replace the hub fallback in README/package metadata with the detail URL and retain an API documentation link.

Source metadata targets `https://github.com/geonodecom/integration-langchain`; the repository remains private until its separate release decision. These local metadata edits do not alter an existing PyPI/npm listing. Carry them into the authoritative publishing source at the coordinated next release, then verify the registry's rendered README, source/issue links and homepage. Keep existing package names, versions and import identifiers unchanged during preparation.
