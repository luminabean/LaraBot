import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class MonsterPark(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="몬파", description="해당 레벨에서 몬스터파크(1~7판)를 돌면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 몬파(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


    @app_commands.command(name="익몬", description="해당 레벨에서 익스트림 몬스터파크를 돌면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 익몬(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


async def setup(bot):
    await bot.add_cog(MonsterPark(bot))