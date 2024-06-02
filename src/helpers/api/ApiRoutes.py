import aiohttp

from logging import getLogger

# Testing
import asyncio
from pprint import pprint

log = getLogger("ApiHandler")

__all__ = ("ApiHandler",)


class ApiHandler:
    def __init__(self, session: aiohttp.ClientSession, key: str):
        self.http = session
        self._headers = {"API-Key": key}

    async def __aenter__(self): ...

    async def __aexit__(self): ...

    async def close(self):
        await self.http.close()

    async def status(self) -> bool:
        ROUTE = "https://api.hypixel.net/v2/punishmentstats"  # Random route to test api key validity

        resp = await self.http.get(ROUTE, headers=self._headers)

        # print(f"Returned {resp.status}")
        json = await resp.json()
        # pprint(json)

        if resp.status == 500:
            log.critical(
                "Could not establish a connection to api.hypixel.net (Code 5xx)"
            )

        if resp.status != 200:
            log.critical(
                "Could not establish a connection to api.hypixel.net (Code 4xx)"
            )
            return False

        elif json["status"] == False:
            return False

        return True
