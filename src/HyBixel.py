import discord
from discord.ext import commands
from discord.utils import setup_logging

from prisma import Prisma

import helpers
from .HyBixelTree import HyBixelTree

setup_logging()


class HyBixel(commands.Cog):
    def __init__(self, *, config: helpers.Config, p: Prisma):
        self.config = config
        self.prisma = p

        intents: discord.Intents = discord.Intents().default()
        intents.members = True

        self.prefix = commands.when_mentioned_or(config.prefix)

        allowed_mentions = discord.AllowedMentions(
            everyone=False, users=True, roles=False
        )

        super().__init__(
            command_prefix=self.prefix,
            intents=intents,
            allowed_mentions=allowed_mentions,
            tree_cls=HyBixelTree,
        )

        self.token = config.token

        self.error_webhook = config.error_webhook

    async def __aenter__(self): ...

    async def __aexit__(self): ...

    async def generateUsernameCache(self):
        # Generate username cache of top 20 most searched usernames.
        ...
        self.cachedNames = await self.prisma.user.find_many(20)
