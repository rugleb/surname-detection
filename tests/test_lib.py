import unittest

from project.lib import ExcludeSchema, StrEnum, is_uuid
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


class IsUUIDTestCase(MainTestCase):

    def test_with_valid_uuid(self) -> None:
        uuid = "42ca9035-42b1-47eb-b2dd-2c3a19dca79f"
        self.assertTrue(is_uuid(uuid))

    def test_with_invalid_uuid(self) -> None:
        uuid = "42ca9035"
        self.assertFalse(is_uuid(uuid))


if __name__ == "__main__":
    unittest.main()
