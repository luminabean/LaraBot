import discord, asyncio
from discord import app_commands
from discord.ext import commands
from discord import Interaction
import pandas as pd

WEAPON_NAME = ["스태프", "ESP리미터", "매직건틀렛", "샤이닝로드", "완드",
               "핸드캐논", "데스페라도", "두손검", "두손도끼", "두손둔기",
               "창", "한손둔기", "한손검", "한손도끼", "석궁",
               "케인", "부채", "듀얼보우건", "활", "단검",
               "에인션트보우", "체인", "폴암", "너클", "소울슈터",
               "에너지소드", "건틀렛리볼버", "건", "아대", "튜너",
               "브레스슈터", "차크람"]

class Option(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="특수무기추옵", description="해방된 카이세리움, 류드의 검, 변질된 알리샤의 스태프, 라이트시커의 추옵 정보를 알려줘요.")
    @app_commands.describe(set_name="무기 이름")
    async def 특수무기추옵(self, interaction: Interaction, set_name: str):
        set_name = set_name.replace(" ", "")

        if set_name == "카세" or set_name == "해방된카이세리움":
            set_name = "해카세"
        if set_name == "류드의검":
            set_name = "류드"
        if set_name == "변질된알리샤의스태프" or set_name == "알리샤스태프":
            set_name = "알리샤"

        file_name = "Database/Option/" + set_name + ".csv"
        table = pd.read_csv(file_name)

        # 특수 아이템의 경우 0번 인덱스 불러오기
        data = table.iloc[0]
        print(f"무기 이름: {set_name} {data[1]}")
        print(f"기본 공격력/마력: {data[2]}")
        print(f"추옵: {data[3]} {data[4]} {data[5]} {data[6]} {data[7]}")

        # 임베드 변수
        embed_title = data[1]
        embed_description = "기본 공격력/마력: " + str(data[2])
        option_msg = f"☆☆☆☆★: {data[3]}\n☆☆☆★★: {data[4]}\n☆☆★★★: {data[5]}\n☆★★★★: {data[6]}\n★★★★★: {data[7]}"

        # 임베드 양식
        embed = discord.Embed(title=embed_title, description=embed_description, color=discord.Color.yellow())
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="추가옵션 정보", value=option_msg, inline=False)

        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="추옵", description="해당 세트 무기의 추옵 정보를 알려줘요. (태도, 대검은 현재 미지원)")
    @app_commands.describe(set_name="세트명", weapon="무기 이름")
    async def 추옵(self, interaction: Interaction, set_name: str, weapon: str):
        set_name = set_name.replace(" ", "")
        weapon = weapon.replace(" ", "")

        # 데이터 불러오기
        if set_name == "포이즈닉":
            set_name = "자쿰"
        if set_name == "힐라":
            set_name = "네크로"
        if set_name == "반레온":
            set_name = "로얄반레온"
        if set_name == "무스펠":
            set_name = "쟈이힌"
        if set_name == "우트" or set_name == "펜살" or set_name == "펜살리르":
            set_name = "우트가르드"
        if set_name == "시그" or set_name == "시그너스" or set_name == "드래곤테일" or set_name == "샤크투스" or set_name == "레이븐혼" or set_name == "라이온하트" or set_name == "팔콘윙":
            set_name = "여제"
        if set_name == "파프" or set_name == "루타" or set_name == "카루타" or set_name == "카룻":
            set_name = "파프니르"
        if set_name == "앱솔":
            set_name = "앱솔랩스"
        if set_name == "앜셰" or set_name == "아케인":
            set_name = "아케인셰이드"
        if set_name == "제네" or set_name == "검은마법사" or set_name == "검마":
            set_name = "제네시스"

        if weapon == "라즐리":
            weapon = "태도"
        if weapon == "라피스":
            weapon = "대검"

        # 태도, 대검이라면 제로 파일 불러오기
        if weapon == "태도" or weapon == "대검":
            file_name = "Database/Option/" + weapon + ".csv"
        else:
            file_name = "Database/Option/" + set_name + ".csv"
        table = pd.read_csv(file_name)
        weapon_idx = WEAPON_NAME.index(weapon)
        print(f"무기 인덱스: {weapon_idx}")

        # 제로라면
        if weapon == "태도" or weapon == "대검":
            if set_name == "앱솔랩스":
                data = table.iloc[7]
            if set_name == "아케인셰이드":
                data = table.iloc[8]
            if set_name == "제네시스":
                data = table.iloc[9]
        else:
            data = table.iloc[weapon_idx]
        print(f"무기 이름: {set_name} {data[1]}")
        print(f"기본 공격력/마력: {data[2]}")
        print(f"추옵: {data[3]} {data[4]} {data[5]} {data[6]} {data[7]}")

        # 임베드 변수
        embed_title = data[1]
        embed_description = "기본 공격력/마력: " + str(data[2])
        option_msg = f"☆☆☆☆★: {data[3]}\n☆☆☆★★: {data[4]}\n☆☆★★★: {data[5]}\n☆★★★★: {data[6]}\n★★★★★: {data[7]}"

        # 임베드 양식
        embed = discord.Embed(title=embed_title, description=embed_description, color=discord.Color.yellow())
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="추가옵션 정보", value=option_msg, inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Option(bot))
