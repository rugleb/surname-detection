import uvloop
from aiohttp import web

from project import settings

from .middlewares import MIDDLEWARES
from .services import SurnameDetector
from .views import ROUTES

__all__ = (
    "create_app",
)

uvloop.install()


async def detector_context(app: web.Application):
    path = settings.STORAGE_DIR.joinpath("surname_detector.pkl")
    detector = SurnameDetector.from_file(path)

    app["detector"] = detector
    yield


async def create_app() -> web.Application:
    app = web.Application(middlewares=MIDDLEWARES)
    app.router.add_routes(ROUTES)

    app.cleanup_ctx.append(detector_context)

    return app
