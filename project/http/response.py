from http import HTTPStatus
from typing import Dict, Optional, Union

import ujson
from aiohttp import hdrs, web
from multidict import CIMultiDict

__all__ = (
    "create_response",
    "ok",
    "bad_request",
    "server_error",
)

HEADERS = CIMultiDict({
    hdrs.EXPIRES: "0",
    hdrs.PRAGMA: "no-cache",
    hdrs.CACHE_CONTROL: "no-cache, no-store, must-revalidate",
    hdrs.CONTENT_ENCODING: "gzip",
})

DEFAULT_DATA = {}


def create_response(http_status: Union[int, HTTPStatus],
                    data: Optional[dict] = None,
                    message: Optional[str] = None) -> web.Response:
    """An HTTP Response instance factory"""

    if not isinstance(http_status, HTTPStatus):
        http_status = HTTPStatus(http_status, None)

    content = {
        "status": http_status < HTTPStatus.BAD_REQUEST,
        "data": data or DEFAULT_DATA,
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
