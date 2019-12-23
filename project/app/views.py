from aiohttp import hdrs, web

from project.http import ok

__all__ = ("routes", )


async def ping(_: web.Request) -> web.Response:
    return ok(message="pong")


routes = (
    web.route(hdrs.METH_ANY, "/ping", ping, name="ping"),
)
