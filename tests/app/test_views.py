import unittest

from aiohttp.test_utils import unittest_run_loop

from project.http import create_response
from tests import MainTestCase


class PingViewTestCase(MainTestCase):
    url = "/ping"

    @unittest_run_loop
    async def test_response_200(self) -> None:
        r = await self.client.get(self.url)

        ok = create_response(200, message="pong")
        await self.assertResponseEqual(ok, r)


if __name__ == "__main__":
    unittest.main()
