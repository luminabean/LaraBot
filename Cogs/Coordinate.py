import discord, asyncio, requests, urllib.request
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from bs4 import BeautifulSoup


class Coordinate(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    # 캐릭터가 존재하는지 확인한다
    def identify_character(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'user-summary-list'라는 클래스가 존재하는가?
            if class_name.startswith('user-summary-list'):
                return name


    @app_commands.command(name="코디", description="해당 캐릭터의 코디 정보를 불러와요.")
    @app_commands.describe(nickname="닉네임")
    async def 코디(self, interaction: Interaction, nickname:str):
        url = "https://maple.gg/u/" + nickname  # maple.gg 캐릭터 정보창

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 존재하는 캐릭터인지 확인
            identifier = soup.find_all(self.identify_character)

            if identifier == []:
                print("검색결과가 없습니다.")
                await interaction.response.send_message(nickname + '님의 정보는 존재하지 않는 것 같아요!')
            else:
                # 정보 크롤링
                world = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > h3 > img')['alt']
                world_img_url = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > h3 > img')['src']
                urllib.request.urlretrieve("https:" + world_img_url, "world.png")
                guild = soup.select_one(
                    '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(1) > a')
                guild = guild.get_text().split()
                guild = guild[0]
                character_img_url = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img')['src']
                urllib.request.urlretrieve(character_img_url, "character.png")
                hat = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(1) > span.character-coord__item-name').get_text()
                hair = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(2) > span.character-coord__item-name').get_text()
                face = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(3) > span.character-coord__item-name').get_text()
                top = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(4) > span.character-coord__item-name').get_text()
                pants = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(5) > span.character-coord__item-name').get_text()
                shoes = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(6) > span.character-coord__item-name').get_text()
                weapon = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items > div:nth-child(7) > span.character-coord__item-name').get_text()

                # 출력 테스트
                print(f"월드: {world}")
                print(f"모자: {hat}")
                print(f"헤어: {hair}")
                print(f"성형: {face}")
                print(f"상의: {top}")
                print(f"하의: {pants}")
                print(f"신발: {shoes}")
                print(f"무기: {weapon}")


                # 임베드 변수
                embed_title = nickname
                embed_description = world
                char_img = discord.File("character.png", filename="char.png")

                # 임베드 양식
                # 제작자 캐릭터면 루미나 그린색
                if nickname == "탠루나" or nickname == "나방콩":
                    embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0x99E593)
                # 리부트는 청록색
                elif world == "리부트":
                    # 제작자가 속한 길드의 유저라면 무궁화색
                    if guild == "미모" or guild == "류도" or guild == "가온누리" or guild == "별다방":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0xE1A8A5)
                    # 제작자 1인 길드 소속 캐릭터면 루미나 그린색
                    elif guild == "심포니":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0x99E593)
                    else:
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=discord.Color.teal())
                elif world == "리부트2":
                    embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=discord.Color.teal())
                # 일반섭은 주황색
                else:
                    # 제작자 1인 길드 소속 캐릭터면 루미나 옐로우색
                    if guild == "루미나" and world == "크로아":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0xE2E276)
                    else:
                        embed = discord.Embed(title=embed_title, url=url, description   =embed_description, color=discord.Color.orange())
                embed.set_thumbnail(url="attachment://char.png")
                embed.add_field(name="", value="", inline=False)
                embed.add_field(name="모자", value=hat, inline=True)
                embed.add_field(name="헤어", value=hair, inline=True)
                embed.add_field(name="성형", value=face, inline=True)
                embed.add_field(name="상의", value=top, inline=True)
                embed.add_field(name="하의", value=pants, inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="신발", value=shoes, inline=True)
                embed.add_field(name="무기", value=weapon, inline=True)
                embed.add_field(name="", value="", inline=True)

                await interaction.response.send_message(nickname + '님의 코디 정보를 불러왔어요!', embed=embed, file=char_img)
        else:
            print(response.status_code)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Coordinate(bot))