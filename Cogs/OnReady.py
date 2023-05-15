import discord, asyncio
from discord.ext import commands

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # bot 활동 상태 관련 변수
    status = discord.Status.online
    activity = discord.Game("개미 먹기")


    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=self.status, activity=self.activity)
        print(f'{self.bot.user.name}이 켜졌습니다!')


async def setup(bot):
    await bot.add_cog(OnReady(bot))