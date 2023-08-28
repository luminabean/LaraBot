import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="도움말", description="도움이 필요하시나요?")
    async def 도움말(self, interaction: Interaction):
        embed = discord.Embed(title="/도움말", description="라라봇의 명령어 모음이에요.", color=discord.Color.yellow())
        embed.add_field(name="", value="")
        embed.add_field(name="/정보 (캐릭터명)", value="해당 캐릭터의 정보(레벨, 길드, 인기도, 랭킹)를 불러와요.", inline=False)
        embed.add_field(name="/무릉 (캐릭터명)", value="해당 캐릭터의 무릉도장 최고기록 정보와 추천 보스 정보를 불러와요.", inline=False)
        embed.add_field(name="/시드 (캐릭터명)", value="해당 캐릭터의 더시드 최고기록 정보를 불러와요.", inline=False)
        embed.add_field(name="/유니온 (캐릭터명)", value="해당 캐릭터의 유니온 정보(유니온 레벨, 전투력, 일간 획득 코인량)를 불러와요.", inline=False)
        embed.add_field(name="/업적 (캐릭터명)", value="해당 캐릭터의 업적 정보를 불러와요.", inline=False)
        embed.add_field(name="/길드 (월드명) (길드명)", value="해당 길드의 정보(길드마스터명, 길드원수, 길드포인트, 랭킹)를 불러와요.", inline=False)
        embed.add_field(name="/코디 (캐릭터명)", value="해당 캐릭터의 코디 정보를 불러와요.", inline=False)
        embed.add_field(name="/추옵 (세트명) (무기 종류)", value="해당 세트 무기의 추옵 정보를 알려줘요. (태도, 대검은 현재 미지원)", inline=False)
        embed.add_field(name="/특수무기추옵 (세트명)", value="해방된 카이세리움, 류드의 검, 변질된 알리샤의 스태프, 라이트시커의 추옵 정보를 알려줘요.", inline=False)
        embed.add_field(name="/로얄 (횟수)", value="해당 횟수만큼 로얄스타일 시뮬레이션을 돌려요. (1, 10, 25, 45개 가능)", inline=False)
        embed.add_field(name="/익성비(성비1, 성비2, 성비3, 태성비, 극성비) (레벨)", value="해당 레벨에서 성장의 비약을 먹으면 경험치가 어느정도 올라가는지 알려줘요.", inline=False)
        embed.add_field(name="/몬파(익몬) (레벨)", value="해당 레벨에서 몬파(1~7판), 익몬(260이상 부터)을 돌면 경험치가 어느정도 올라가는지 알려줘요.", inline=False)
        embed.add_field(name="/일퀘 (레벨)", value="해당 레벨에서 아케인/어센틱 지역 일퀘를 하면 경험치가 어느정도 올라가는지 알려줘요. (200~289 레벨만 지원)", inline=False)
        embed.add_field(name="/보스 (난이도) (보스명)", value="해당 보스의 정보(레벨, 체력, 방어율, 포스, 보상)를 알려줘요.", inline=False)
        embed.add_field(name="/tmi", value="라라봇이 쓸모없는 TMI 정보를 알려줘요.", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.set_footer(text="이 외에도 숨겨진 명령어가 존재해요! (숨겨진 명령어는 !로 시작해요)")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))