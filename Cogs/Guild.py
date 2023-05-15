import discord, asyncio, requests, urllib.request
from discord.ext import commands
from bs4 import BeautifulSoup

WORLDS = {"스카니아": "scania", "베라": "bera", "루나": "luna",
           "제니스": "zenith", "크로아": "croa", "유니온": "union",
           "엘리시움": "elysium", "이노시스": "enosis", "레드": "red",
           "오로라": "aurora", "아케인": "arcane", "노바": "nova",
           "리부트": "reboot", "리부트2": "reboot2"}


class Guild(commands.Cog, name="길드"):
    def __init__(self, bot):
        self.bot = bot


    # 길드가 존재하는지 확인한다
    def identify_guild(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'card-header'라는 클래스가 존재하는가?
            if class_name.startswith('view-error'):
                return name


    @commands.command(name="길드")
    async def character(self, ctx, world, name):
        # 월드명 중복 처리
        if world == "스카":
            world = "스카니아"
        if world == "엘슘":
            world = "엘리시움"
        if world == "리부트1" or world == "리부트 1":
            world = "리부트"
        if world == "리부트 2":
            world = "리부트2"

        # 순서를 바꿔서 입력
        if world not in WORLDS.keys():
            print("순서를 바꿔서 입력한 듯...?")
            await ctx.send("'!길드 (월드명) (길드명)' 순서대로 입력하셨나요? 제대로 입력해주세요!")

        url = "https://maple.gg/guild/" + WORLDS[world] + "/" + name  # maple.gg 길드 정보창
        print(url)

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 존재하는 길드인지 확인
            identifier = soup.find_all(self.identify_guild)
            print(identifier)

            if identifier != []:
                print("검색결과가 없습니다.")
                await ctx.send(world + " 월드에는 " + name + ' 길드가 존재하지 않는 것 같아요!')
            else:
                # 정보 크롤링
                master = soup.select_one('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div:nth-child(1) > span > a').get_text()
                population = soup.select_one('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div:nth-child(4) > span').get_text()
                gp = soup.select_one('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div:nth-child(5) > span').get_text()
                ranking = soup.select_one('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div:nth-child(3) > span').get_text()
                ranking_world = soup.select_one('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div:nth-child(2) > span').get_text()

                # 출력 테스트
                print(f"월드: {world}")
                print(f"길드명: {name}")
                print(f"길드마스터: {master}")
                print(f"길드원수: {population}")
                print(f"길드포인트: {gp}")
                print(f"전체랭킹: {ranking}")
                print(f"월드랭킹: {ranking_world}")

                # 임베드 변수
                embed_title = name
                embed_description = world

                # 임베드 양식
                # 월드에 따라 색깔 다르게
                embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0x000000)
                embed.add_field(name="", value="")
                embed.add_field(name="길드마스터", value=master, inline=False)
                embed.add_field(name="길드원수", value=population, inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="길드포인트", value=gp, inline=True)
                embed.add_field(name="전체랭킹", value=ranking.replace("\n", ""), inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="월드랭킹", value=ranking_world, inline=True)
                embed.add_field(name="", value="")


                await ctx.send(world + " 월드 " + name + '길드의 정보를 불러왔어요!')
                await ctx.channel.send(embed=embed)
        else:
            print(response.status_code)


async def setup(bot):
    await bot.add_cog(Guild(bot))