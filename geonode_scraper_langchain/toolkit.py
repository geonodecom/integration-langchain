from __future__ import annotations

import asyncio
from typing import Any, Sequence

from geonode_scraper_tools_core import ScraperToolService, ScraperToolSettings, get_operations
from geonode_scraper_tools_core.registry import OperationSpec


class ScraperLangChainToolkit:
    def __init__(self, service: ScraperToolService) -> None:
        self.service = service

    @classmethod
    def from_settings(cls, settings: ScraperToolSettings) -> ScraperLangChainToolkit:
        return cls(ScraperToolService(settings, client=_client()))

    def get_tools(self, operations: Sequence[str] | None = None) -> list[Any]:
        from langchain_core.tools import StructuredTool

        return [
            self._build_tool(StructuredTool=StructuredTool, operation=operation)
            for operation in get_operations(operations)
        ]

    def _build_tool(self, *, StructuredTool: type[Any], operation: OperationSpec) -> Any:
        def _invoke(**kwargs: Any) -> dict[str, Any]:
            return operation.invoke(self.service, **kwargs)

        async def _ainvoke(**kwargs: Any) -> dict[str, Any]:
            return await asyncio.to_thread(operation.invoke, self.service, **kwargs)

        _invoke.__name__ = operation.tool_name
        _invoke.__doc__ = operation.description

        return StructuredTool.from_function(
            func=_invoke,
            coroutine=_ainvoke,
            name=operation.tool_name,
            description=operation.description,
            args_schema=operation.args_schema,
        )


def build_langchain_tools(
    *,
    settings: ScraperToolSettings | None = None,
    service: ScraperToolService | None = None,
    operations: Sequence[str] | None = None,
) -> list[Any]:
    resolved_service = _resolve_service(settings=settings, service=service)
    return ScraperLangChainToolkit(resolved_service).get_tools(operations=operations)


def _resolve_service(
    *,
    settings: ScraperToolSettings | None,
    service: ScraperToolService | None,
) -> ScraperToolService:
    if service is not None:
        return service
    if settings is None:
        raise ValueError("Provide either settings or service to build LangChain tools.")
    return ScraperToolService(settings, client=_client())


def _client() -> str:
    # The API labels requests from this package `langchain` (scraper-api#674).
    from . import __version__

    return f"geonode-langchain/{__version__}"
