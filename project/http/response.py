from http import HTTPStatus
from typing import Dict, Optional

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
                    data: Optional[dict] = None,
                    message: Optional[str] = None) -> web.Response:
    """Create a new JSON Response class instance."""

    # noinspection PyArgumentList
    http_status = HTTPStatus(code)

    content = {
        "status": http_status < HTTPStatus.BAD_REQUEST,
        "data": data or {},
        "message": message or http_status.phrase,
    }

    return web.json_response(content, headers=HEADERS, dumps=ujson.dumps)


def ok(data: Dict = None, message: str = None) -> web.Response:
    http_status = HTTPStatus.OK
    return create_response(http_status, data, message)


def bad_request(data: Dict = None, message: str = None) -> web.Response:
    http_status = HTTPStatus.BAD_REQUEST
    return create_response(http_status, data, message)


def server_error(data: Dict = None, message: str = None) -> web.Response:
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    return create_response(http_status, data, message)
