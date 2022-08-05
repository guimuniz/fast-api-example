# import logging
import json

import httpx
from fastapi_utils.enums import StrEnum

from app.client.exceptions import BadGatewayException
from app.core.config import Settings


class HttpMethods(StrEnum):
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"


settings = Settings()


class Client:
    def __init__(self):
        self.base_url = settings.BASE_URL

    async def _do_request(self, *, method: HttpMethods, url: str, body: dict | None = None):
        client = getattr(httpx.AsyncClient(), method.value)
        args = {
            "url": f'{self.base_url}{url}',
            "timeout": 15,
            "auth": "",
        }
        if body:
            args["data"] = json.dumps(body)
        try:
            response = await client(**args)
        except (httpx.ConnectError, httpx.TimeoutException) as ex:
            raise BadGatewayException(f'Communication error. Error: {ex}')

        if response.status_code != 200:
            raise Exception(response.json())

        return response.json()

    async def root(self):
        return await self._do_request(method=HttpMethods.GET, url="/")
