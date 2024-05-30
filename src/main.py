from HyBixel import HyBixel
from prisma import Prisma
from helpers import Config

import asyncio


async def run():
    config = Config().init()
    async with Prisma() as p:
        await p.connect()
