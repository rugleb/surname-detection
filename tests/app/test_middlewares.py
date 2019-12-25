import unittest

from aiohttp import web
from aiohttp.test_utils import unittest_run_loop

from project.http import create_response
from tests import MainTestCase


class MiddlewaresTestCase(MainTestCase):
    url = "/error"

    async def get_application(self) -> web.Application:
        app = await super().get_application()

        async def error(_: web.Request):
            return 1 / 0

        app.router.add_get("/error", error)
        return app

    @unittest_run_loop
    async def test_request_id_handler(self) -> None:
        request_ids = []

        for _ in range(3):
            r = await self.client.get("/ping")

            request_id = r.headers["X-Request-Id"]
            self.assertUUID(request_id)

            request_ids.append(request_id)

        self.assertHasNotDuplicates(request_ids)

    @unittest_run_loop
    async def test_normalize_path_middleware(self) -> None:
        r = await self.client.get("/ping/")

        ok = create_response(200, message="pong")
        await self.assertResponseEqual(ok, r)

    @unittest_run_loop
    async def test_default_error_handler(self) -> None:
        r = await self.client.get(self.url)

        server_error = create_response(500)
        await self.assertResponseEqual(server_error, r)

    @unittest_run_loop
    async def test_client_error_handler(self) -> None:
        r = await self.client.get("/undefined")

        not_found = create_response(404)
        await self.assertResponseEqual(not_found, r)


if __name__ == "__main__":
    unittest.main()
