from HyBixel import HyBixel
from prisma import Prisma
from helpers import Config, api

import asyncio
import aiohttp


async def run():
    config = Config().init()
    async with aiohttp.ClientSession() as session:
        async with Prisma() as p, api.ApiHandler(session, config.api_key) as apihandler:
            await p.connect()
            async with HyBixel(config=config, p=p, apihandler=apihandler) as bot:
                await bot.start()
