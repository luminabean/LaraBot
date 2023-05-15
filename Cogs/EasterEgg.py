import discord, asyncio, random
from discord.ext import commands

class EasterEgg(commands.Cog, name="이스터에그"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="바보")
    async def fool(self, ctx):
        await ctx.send('저 바보 아니라구욧! ㅜㅜ')


    @commands.command(name="빛콩")
    async def luminabean(self, ctx):
        await ctx.send('어라...? 개발자님을 아시나요?')


    @commands.command(name="콩눈나")
    async def sisterbean(self, ctx):
        await ctx.send('개발자님은 남자라구요 ㅜㅜ')


    @commands.command(name="햇무니")
    async def munie(self, ctx):
        await ctx.send('햇무니...? 평행세계에 있는 저의 이름인가요?')


    @commands.command(name="루시드")
    async def lucid(self, ctx):
        await ctx.send("개발자님은 가끔 저에게 '루시드 얼굴 죠아!'라고 외치셨어요.")


    @commands.command(name="라라")
    async def lara(self, ctx):
        rand = random.randrange(1, 92)

        if rand >= 1 and rand <= 15:
            await ctx.send('바람을 타고 놀자~')
        if rand >= 16 and rand <= 30:
            await ctx.send('따스한 햇살은 기분 좋아~')
        if rand >= 31 and rand <= 45:
            await ctx.send('바람은 정말 못말려~')
        if rand >= 46 and rand <= 60:
            await ctx.send('볼이 빵빵!')
        if rand >= 61 and rand <= 75:
            await ctx.send('신나게 달려 보자!')
        if rand >= 76 and rand <= 90:
            await ctx.send('들어 봐, 땅의 목소리를!')
        if rand == 91:
            await ctx.send('라라는 바보야? 네~!')


    @commands.command(name="그리")
    async def gri(self, ctx):
        await ctx.send('그리는 제일 좋은 친구에요! 가끔씩 툴툴대긴 하지만요...')


    @commands.command(name="창섭")
    async def changseop(self, ctx):
        await ctx.send('어라...? 창섭은 저희 아빠 성함이에요!')


async def setup(bot):
    await bot.add_cog(EasterEgg(bot))