import discord, asyncio
from discord import app_commands
from discord.ext import commands
from discord import Interaction
import pandas as pd

class DailyQuest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="일퀘", description="해당 레벨에서 아케인/어센틱 지역 일퀘를 하면 경험치가 어느정도 올라가는지 알려줘요. (200~289 레벨만 지원)")
    @app_commands.describe(level="레벨")
    async def 일퀘(self, interaction: Interaction, level: int):
        # 파일 불러오기
        file_name = "Database/DailyQuest/일퀘.csv"

        table = pd.read_csv(file_name)
        print(f"레벨 인덱스: {level - 200}")
        data = table.iloc[level - 200]

        print(f"레벨: {level}")
        print(f"아케인: {data[2]} {data[3]} {data[4]} {data[5]} {data[6]} {data[7]}")
        print(f"테네브리스: {data[8]} {data[9]} {data[10]}")
        print(f"그란디스: {data[11]} {data[12]} {data[13]} {data[14]} {data[15]} {data[16]}")

        # 임베드 변수
        embed_title = str(level) + "레벨일 때 일일퀘스트를 클리어하면?"
        embed_description = "이 만큼의 경험치를 얻을 수 있어요!"

        # 일퀘 경험치 메시지
        arcane_sum = 0.000
        tenebris_sum = 0.000
        grandis_sum = 0.000

        arcane_river_msg = f"여로: {data[2]:.3f}%\n"
        arcane_sum += data[2]

        if level >= 210:
            arcane_river_msg += f"츄츄: {data[3]:.3f}%\n"
            arcane_sum += data[3]
        if level >= 220:
            arcane_river_msg += f"레헬른: {data[4]:.3f}%\n"
            arcane_sum += data[4]
        if level >= 225:
            arcane_river_msg += f"아르카나: {data[5]:.3f}%\n"
            arcane_sum += data[5]
        if level >= 230:
            arcane_river_msg += f"모라스: {data[6]:.3f}%\n"
            arcane_sum += data[6]
        if level >= 235:
            arcane_river_msg += f"에스페라: {data[7]:.3f}%\n"
            arcane_sum += data[7]
        sum_msg = f"아케인 리버: {arcane_sum:.3f}%\n"

        if level >= 245:
            tenebris_msg = f"문브릿지: {data[8]:.3f}%\n"
            tenebris_sum += data[8]
        if level >= 250:
            tenebris_msg += f"미궁: {data[9]:.3f}%\n"
            tenebris_sum += data[9]
        if level >= 255:
            tenebris_msg += f"리멘: {data[10]:.3f}%\n"
            tenebris_sum += data[10]
        if level >= 245:
            sum_msg += f"테네브리스: {tenebris_sum:.3f}%\n"

        if level >= 260:
            grandis_msg = f"세르니움: {data[11]:.3f}%\n"
            grandis_sum += data[11]
        if level >= 265:
            grandis_msg += f"아르크스: {data[12]:.3f}%\n"
            grandis_sum += data[12]
        if level >= 270:
            grandis_msg += f"오디움: {data[13]:.3f}%\n"
            grandis_sum += data[13]
        if level >= 275:
            grandis_msg += f"도원경: {data[14]:.3f}%\n"
            grandis_sum += data[14]
        if level >= 280:
            grandis_msg += f"아르테리아: {data[15]:.3f}%\n"
            grandis_sum += data[15]
        if level >= 285:
            grandis_msg += f"카르시온: {data[16]:.3f}%\n"
            grandis_sum += data[16]
        if level >= 260:
            sum_msg += f"그란디스: {grandis_sum:.3f}%\n"
        sum_msg += f"총: {arcane_sum + tenebris_sum + grandis_sum:.3f}%\n"

        # 임베드 양식
        embed = discord.Embed(title=embed_title, description=embed_description, color=discord.Color.yellow())
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="아케인 리버 지역", value=arcane_river_msg, inline=False)
        embed.add_field(name="", value="", inline=False)

        if level >= 245:
            embed.add_field(name="테네브리스 지역", value=tenebris_msg, inline=False)
            embed.add_field(name="", value="", inline=False)
        if level >= 260:
            embed.add_field(name="그란디스 지역", value=grandis_msg, inline=False)
            embed.add_field(name="", value="", inline=False)

        embed.add_field(name="합계", value=sum_msg, inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(DailyQuest(bot))