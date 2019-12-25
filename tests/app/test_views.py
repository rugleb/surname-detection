import unittest

from aiohttp.test_utils import unittest_run_loop

from project.http import bad_request, ok
from tests import MainTestCase


class PingViewTestCase(MainTestCase):
    url = "/ping"

    @unittest_run_loop
    async def test_response_200(self) -> None:
        actual = await self.client.get(self.url)

        expected = ok(message="pong")
        await self.assertResponseEqual(expected, actual)


class DetectViewTestCase(MainTestCase):
    url = "/detect"

    @unittest_run_loop
    async def test_response_200(self) -> None:
        params = {
            "surname": "Карпушкин",
        }
        actual = await self.client.get(self.url, params=params)

        data = {
            "confidence": 0.3859428555,
        }
        expected = ok(data)
        await self.assertResponseEqual(expected, actual)

    @unittest_run_loop
    async def test_response_400(self) -> None:
        actual = await self.client.get(self.url)

        data = {
            "errors": {
                "surname": ["Missing data for required field."],
            },
        }
        expected = bad_request(data, "Input payload validation failed.")
        await self.assertResponseEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
