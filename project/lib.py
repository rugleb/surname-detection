from enum import Enum
from uuid import UUID

from marshmallow import EXCLUDE, Schema

__all__ = (
    "ExcludeSchema",
    "StrEnum",
    "is_uuid",
)


class ExcludeSchema(Schema):
    """Excluded all unknown fields"""

    class Meta:
        unknown = EXCLUDE


class StrEnum(str, Enum):

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__


def is_uuid(value: str, version: int = 4) -> bool:
    try:
        uuid = UUID(value, version=version)
    except ValueError:
        return False
    return str(uuid) == value
