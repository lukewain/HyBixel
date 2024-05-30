from src.HyBixel import HyBixel

from .GuildAdmin import GuildAdmin


class Admin(GuildAdmin):
    """Admin cog for the bot"""


async def setup(bot: HyBixel):
    await bot.add_cog(Admin(bot))
