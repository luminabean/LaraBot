import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class Boss(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="보스", description="해당 보스의 정보(레벨, 체력, 방어율, 포스, 보상)를 알려줘요.")
    @app_commands.describe(difficulty="난이도", boss_name="보스명")
    async def 보스(self, interaction: Interaction, difficulty: str, boss_name: str):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


async def setup(bot):
    await bot.add_cog(Boss(bot))