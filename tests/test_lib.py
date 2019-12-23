import unittest

from project.lib import ExcludeSchema, StrEnum
from tests import MainTestCase


class ExcludeSchemaTestCase(MainTestCase):
    schema = ExcludeSchema()

    def test_with_empty_data(self) -> None:
        data = {}

        serialized = self.schema.load(data)
        self.assertDictEqual(data, serialized)

    def test_with_extra_keys(self) -> None:
        data = {
            "key": "value",
        }

        serialized = self.schema.load(data)
        self.assertDictEmpty(serialized)


class Colors(StrEnum):
    RED = "red"
    BLUE = "blue"


class StrEnumTestCase(MainTestCase):

    def test_on_isinstance(self) -> None:
        color = Colors.RED
        self.assertIs(color, Colors.RED)

        self.assertEqual("red", color)
        self.assertIsInstance(color, str)


if __name__ == "__main__":
    unittest.main()
