import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class RoyalStyle(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="로얄", description="해당 횟수만큼 로얄스타일 시뮬레이션을 돌려요. (1, 10, 25, 45개 가능)")
    @app_commands.describe(times="횟수")
    async def 로얄(self, interaction: Interaction, times: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


async def setup(bot):
    await bot.add_cog(RoyalStyle(bot))