import uvloop
from aiohttp import web

from .middlewares import middlewares
from .views import routes

__all__ = (
    "create_app",
)

uvloop.install()


async def create_app() -> web.Application:
    app = web.Application(middlewares=middlewares)
    app.router.add_routes(routes)
    return app
