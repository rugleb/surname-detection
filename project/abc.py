from abc import abstractmethod
from typing import Dict

__all__ = (
    "Dictable",
)


class Dictable:

    @abstractmethod
    def to_dict(self) -> Dict:
        pass
