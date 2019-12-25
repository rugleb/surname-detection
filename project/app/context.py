from contextvars import ContextVar

__all__ = (
    "REQUEST_ID",
)

REQUEST_ID: ContextVar[str] = ContextVar("request_id", default="-")
