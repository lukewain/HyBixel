from src.HyBixel import HyBixel


class Admin:
    """Admin cog for the bot"""


async def setup(bot: HyBixel):
    await bot.add_cog(Admin(bot))
