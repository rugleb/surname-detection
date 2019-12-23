import unittest

from marshmallow import ValidationError

from project.app import SurnameSchema
from tests import MainTestCase


class SurnameSchemaTestCase(MainTestCase):
    schema = SurnameSchema()

    def test_with_valid_data(self) -> None:
        data = {
            "surname": "Карпушкин",
        }

        serialized = self.schema.load(data)
        self.assertDictEqual(data, serialized)

    def test_with_empty_data(self) -> None:
        data = {}

        try:
            self.schema.load(data)
        except ValidationError as e:
            self.assertDictEmpty(e.valid_data)

            messages = {
                "surname": ["Missing data for required field."],
            }
            self.assertDictEqual(messages, e.messages)

    def test_with_nullable_surname(self) -> None:
        data = {
            "surname": None,
        }

        try:
            self.schema.load(data)
        except ValidationError as e:
            self.assertDictEmpty(e.valid_data)

            messages = {
                "surname": ["Field may not be null."],
            }
            self.assertDictEqual(messages, e.messages)


if __name__ == "__main__":
    unittest.main()
