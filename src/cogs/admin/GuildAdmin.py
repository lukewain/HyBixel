import discord
from discord import app_commands
from discord.ext import commands

from src.HyBixel import HyBixel

__all__ = ("GuildAdmin",)


class GuildAdmin(commands.Cog):
    def __init__(self, bot: HyBixel):
        self.bot = bot

    @app_commands.command(name="info")
    async def adminInfo(self, itr: discord.Interaction[HyBixel]):
        ...
        # Info showing status of Hypixel connection, discord latency, current servers, members, *rate limit queue size

        e = discord.Embed(title="Bot Info")

        # Get the Hypixel Connection status
        "Hypixel connection: Circle emoji"
        status = await itr.client.apihandler.status()
