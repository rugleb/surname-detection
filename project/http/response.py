from http import HTTPStatus
from typing import Any

import ujson
from aiohttp import hdrs, web

from project.types import Headers

__all__ = (
    "create_response",
    "ok",
    "bad_request",
    "server_error",
)

HEADERS: Headers = {
    hdrs.EXPIRES: "0",
    hdrs.PRAGMA: "no-cache",
    hdrs.CACHE_CONTROL: "no-cache, no-store, must-revalidate",
}


def create_response(code: int,
                    data: Any = None,
                    message: str = None) -> web.Response:
    """Create a new JSON Response class instance."""

    # noinspection PyArgumentList
    http_status = HTTPStatus(code)

    if not data:
        data = {}

    if not message:
        message = http_status.phrase

    content = {
        "status": http_status < HTTPStatus.BAD_REQUEST,
        "data": data,
        "message": message,
    }

    return web.json_response(content, headers=HEADERS, dumps=ujson.dumps)


def ok(data: Any = None, message: str = None) -> web.Response:
    http_status = HTTPStatus.OK
    return create_response(http_status, data, message)


def bad_request(data: Any = None, message: str = None) -> web.Response:
    http_status = HTTPStatus.BAD_REQUEST
    return create_response(http_status, data, message)


def server_error(data: Any = None, message: str = None) -> web.Response:
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    return create_response(http_status, data, message)
