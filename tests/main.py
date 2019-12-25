from typing import Mapping, Sized

from aiohttp import client, web
from aiohttp.test_utils import AioHTTPTestCase

from project.app import create_app
from project.lib import is_uuid

__all__ = (
    "MainTestCase",
)


class MainTestCase(AioHTTPTestCase):

    async def get_application(self) -> web.Application:
        app = await create_app()
        return app

    def assertDictEmpty(self, value: dict) -> None:
        self.assertDictEqual({}, value)

    def assertListEmpty(self, value: list) -> None:
        self.assertListEqual([], value)

    def assertUUID(self, value: str, *, version: int = 4) -> None:
        self.assertTrue(is_uuid(value), version)

    def assertLenEqual(self, first: Sized, second: Sized) -> None:
        a = len(first)
        b = len(second)
        self.assertEqual(a, b)

    def assertHasNotDuplicates(self, it: list) -> None:
        self.assertLenEqual(it, set(it))

    def assertSubset(self, first: Mapping, second: Mapping) -> None:
        for k, v in first.items():
            self.assertIn(k, second)
            self.assertEqual(v, second[k])

    async def assertResponseEqual(self,
                                  expected: web.Response,
                                  actual: client.ClientResponse) -> None:
        self.assertEqual(expected.status, actual.status)

        json = await actual.json()
        self.assertIsInstance(json, dict)

        text = await actual.text()
        self.assertEqual(expected.text, text)

        self.assertEqual(expected.charset, actual.charset)
        self.assertEqual(expected.content_length, actual.content_length)
        self.assertEqual(expected.content_type, actual.content_type)
        self.assertEqual(expected.reason, actual.reason)

        self.assertSubset(expected.headers, actual.headers)
