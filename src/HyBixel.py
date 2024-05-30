import discord
from discord.ext import commands
from discord.utils import setup_logging

from prisma import Prisma

import helpers

setup_logging()


class HyBixel(commands.Cog):
    def __init__(self, *, config: helpers.Config, p: Prisma):
        self.config = config
        self.prisma = p

        # Checks to be run when needed

    async def __aenter__(self): ...

    async def __aexit__(self): ...

    async def generateUsernameCache(self):
        # Generate username cache of top 20 most searched usernames.
        ...
        self.cachedNames = await self.prisma.user.find_many(20)
