import discord, asyncio, os
from dotenv import load_dotenv
from discord.ext import commands

# bot 관련 변수
load_dotenv()
TOKEN = os.getenv('TOKEN')
command_prefix = '!'
intents = discord.Intents.all()

# bot
bot = commands.Bot(command_prefix=command_prefix, intents=intents)

# Cogs 관련 변수
cogs_path = "Cogs"
abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             cogs_path)


# Cog 파일 로드
async def load():
  for file in os.listdir(abs_cogs_path):
    if file.endswith(".py"):
      await bot.load_extension(f"Cogs.{file[:-3]}")
      print(f"{file[:-3]}을 로드했습니다.")


async def main():
  await load()
  await bot.start(TOKEN)



if __name__ == "__main__":
  asyncio.run(main())
