from __future__ import annotations

from typing import TYPE_CHECKING

import discord
from discord import app_commands


if TYPE_CHECKING:
    from .HyBixel import HyBixel


class HyBixelTree(app_commands.CommandTree):
    async def on_error(
        self,
        interaction: discord.Interaction[HyBixel],
        error: app_commands.AppCommandError,
        /,
    ) -> None:
        return await super().on_error(interaction, error)
