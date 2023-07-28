import discord, asyncio, random
from discord.ext import commands

class Help(commands.Cog, name="도움말"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="도움말")
    async def help(self, ctx):
        embed = discord.Embed(title="도움말", description="라라봇의 명령어 모음이에요.", color=discord.Color.yellow())
        embed.add_field(name="", value="")
        embed.add_field(name="!정보 (캐릭터명)", value="해당 캐릭터의 정보(레벨, 길드, 인기도, 랭킹)를 불러와요.", inline=False)
        embed.add_field(name="!무릉 (캐릭터명)", value="해당 캐릭터의 무릉도장 최고기록 정보와 추천 보스 정보를 불러와요.", inline=False)
        embed.add_field(name="!시드 (캐릭터명)", value="해당 캐릭터의 더시드 최고기록 정보를 불러와요.", inline=False)
        embed.add_field(name="!유니온 (캐릭터명)", value="해당 캐릭터의 유니온 정보(유니온 레벨, 전투력, 일간 획득 코인량)를 불러와요.", inline=False)
        embed.add_field(name="!업적 (캐릭터명)", value="해당 캐릭터의 업적 정보를 불러와요.", inline=False)
        embed.add_field(name="!길드 (월드명) (길드명)", value="해당 길드의 정보(길드마스터명, 길드원수, 길드포인트, 랭킹)를 불러와요.", inline=False)
        embed.add_field(name="!코디 (캐릭터명)", value="해당 캐릭터의 코디 정보를 불러와요.", inline=False)
        embed.add_field(name="!추옵 (세트명) (무기 종류)", value="해당 세트 무기의 추옵 정보를 알려줘요. (태도, 대검은 현재 미지원)", inline=False)
        embed.add_field(name="!TMI", value="라라봇이 쓸데없는 TMI 정보를 알려줘요.", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.set_footer(text="이 외에도 숨겨진 명령어가 존재해요!")

        await ctx.channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))