from aiohttp import hdrs, web

from project.http import ok

from .schemas import SurnameSchema

__all__ = ("ROUTES",)


async def ping(_: web.Request) -> web.Response:
    return ok(message="pong")


async def detect(request: web.Request) -> web.Response:
    detector = request.app["detector"]
    surname = SurnameSchema().load(request.query).pop("surname")
    prediction = detector.predict(surname)
    data = prediction.to_dict()
    return ok(data)


ROUTES = (
    web.route(hdrs.METH_ANY, "/ping", ping, name="ping"),
    web.route(hdrs.METH_GET, "/detect", detect, name="detect"),
)
