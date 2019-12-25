from typing import Awaitable, Callable

from aiohttp import web

__all__ = (
    "Handler",
)

Handler = Callable[[web.Request], Awaitable[web.Response]]
