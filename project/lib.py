from enum import Enum

from marshmallow import EXCLUDE, Schema

__all__ = (
    "ExcludeSchema",
    "StrEnum",
)


class ExcludeSchema(Schema):
    """Excluded all unknown fields"""

    class Meta:
        unknown = EXCLUDE


class StrEnum(str, Enum):

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__
