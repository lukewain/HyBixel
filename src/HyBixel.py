import discord
from discord.ext import commands
from discord.utils import setup_logging

import asyncpg

import helpers

setup_logging()


class HyBixel(commands.Cog):
    def __init__(self, *, config: helpers.Config, pool: asyncpg.Pool[asyncpg.Record]):
        self.config = config
        self.pool = pool

        # Checks to be run when needed

    async def __aenter__(self): ...

    async def __aexit__(self): ...

    async def generateUsernameCache(self):
        # Generate username cache of top 20 most searched usernames.
        ...
