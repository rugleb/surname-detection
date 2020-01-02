from uuid import uuid4

from aiohttp import web
from marshmallow import ValidationError

from project.http import response
from project.types import Handler

from . import context

__all__ = ("MIDDLEWARES",)


def create_request_id() -> str:
    uuid = uuid4()
    return str(uuid)


@web.middleware
async def request_id_handler(request: web.Request, handler: Handler):
    request_id = create_request_id()
    token = context.REQUEST_ID.set(request_id)
    r = await handler(request)
    context.REQUEST_ID.reset(token)
    r.headers["X-Request-Id"] = request_id
    return r


@web.middleware
async def default_error_handler(request: web.Request, handler: Handler):
    try:
        return await handler(request)
    except Exception as e:
        name = e.__class__.__name__
        request.app.logger.error(f"Caught unhandled {name} exception: {e}")
        return response.server_error()


@web.middleware
async def client_error_handler(request: web.Request, handler: Handler):
    try:
        return await handler(request)
    except web.HTTPClientError as e:
        return response.create_response(e.status)


@web.middleware
async def validation_error_handler(request: web.Request, handler: Handler):
    try:
        return await handler(request)
    except ValidationError as e:
        message = "Input payload validation failed."
        return response.bad_request({"errors": e.messages}, message)


MIDDLEWARES = (
    web.normalize_path_middleware(append_slash=False, remove_slash=True),
    request_id_handler,
    default_error_handler,
    client_error_handler,
    validation_error_handler,
)
