import unittest

from project.lib import ExcludeSchema
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


if __name__ == "__main__":
    unittest.main()
