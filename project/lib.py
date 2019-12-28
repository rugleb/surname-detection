import pickle
from enum import Enum
from pathlib import Path
from typing import Any
from uuid import UUID

from marshmallow import EXCLUDE, Schema

__all__ = (
    "ExcludeSchema",
    "StrEnum",
    "is_uuid",
    "read_pickle_file",
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


def read_pickle_file(path: Path, mode: str = "rb") -> Any:
    with path.open(mode) as f:
        return pickle.load(f)
