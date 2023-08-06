import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class DailyQuest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="일퀘", description="해당 레벨에서 아케인/어센틱 지역 일퀘를 하면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 일퀘(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


async def setup(bot):
    await bot.add_cog(DailyQuest(bot))