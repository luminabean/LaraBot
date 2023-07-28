import discord, asyncio, random
from discord.ext import commands
import pandas as pd

WEAPON_NAME = ["스태프", "ESP리미터", "매직건틀렛", "샤이닝로드", "완드",
               "핸드캐논", "데스페라도", "두손검", "두손도끼", "두손둔기",
               "창", "한손둔기", "한손검", "한손도끼", "석궁",
               "케인", "부채", "듀얼보우건", "활", "단검",
               "에인션트보우", "체인", "폴암", "너클", "소울슈터",
               "에너지소드", "건틀렛리볼버", "건", "아대", "튜너",
               "브레스슈터", "차크람"]

class Option(commands.Cog, name="추옵"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="추옵")
    async def option(self, ctx, set_name, weapon):
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

        if set_name == "카세" or set_name == "해방된카이세리움":
            set_name = "해카세"
        if set_name == "류드의검":
            set_name = "류드"
        if set_name == "변질된알리샤의스태프" or set_name == "알리샤스태프":
            set_name = "알리샤"

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

        # 특수 아이템의 경우 0번 인덱스 불러오기
        if set_name == "해카세" or set_name == "라이트시커" or set_name == "알리샤" or set_name == "류드":
            data = table.iloc[0]
        # 제로라면
        elif weapon == "태도" or weapon == "대검":
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

        # 임베드 양식
        embed = discord.Embed(title=embed_title, description=embed_description, color=discord.Color.yellow())
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="★☆☆☆☆", value=data[3], inline=False)
        embed.add_field(name="★★☆☆☆", value=data[4], inline=False)
        embed.add_field(name="★★★☆☆", value=data[5], inline=False)
        embed.add_field(name="★★★★☆", value=data[6], inline=False)
        embed.add_field(name="★★★★★", value=data[7], inline=False)

        await ctx.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Option(bot))
