import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class EXPPotion(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="익성비", description="해당 레벨에서 익스트림 성장의 비약을 먹으면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 익성비(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


    @app_commands.command(name="성비1", description="해당 레벨에서 성장의 비약 (200~209)을 먹으면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 성비1(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


    @app_commands.command(name="성비2", description="해당 레벨에서 성장의 비약 (210~219)을 먹으면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 성비2(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


    @app_commands.command(name="성비3", description="해당 레벨에서 성장의 비약 (220~229)을 먹으면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 성비3(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


    @app_commands.command(name="태성비", description="해당 레벨에서 태풍 성장의 비약을 먹으면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 태성비(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


    @app_commands.command(name="극성비", description="해당 레벨에서 극한 성장의 비약을 먹으면 경험치가 어느정도 올라가는지 알려줘요.")
    @app_commands.describe(level="레벨")
    async def 극성비(self, interaction: Interaction, level: int):
        await interaction.response.send_message("해당 기능은 미구현이에요 ㅜㅜ")


async def setup(bot):
    await bot.add_cog(EXPPotion(bot))