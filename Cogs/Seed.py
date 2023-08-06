import discord, asyncio, requests, urllib.request
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from bs4 import BeautifulSoup


class Seed(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    # 캐릭터가 존재하는지 확인한다
    def identify_character(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'user-summary-list'라는 클래스가 존재하는가?
            if class_name.startswith('user-summary-list'):
                return name


    # 정보가 존재하는지 확인한다
    def identify_info(self, soup):
        seed_class = soup.find_all(class_="col-lg-3 col-6 mt-3 px-1")[1]
        return seed_class.find(class_="user-summary-floor font-weight-bold")

    @app_commands.command(name="시드", description="해당 캐릭터의 더시드 최고기록 정보를 불러와요.")
    @app_commands.describe(nickname="닉네임")
    async def 시드(self, interaction: Interaction, nickname: str):
        url = "https://maple.gg/u/" + nickname  # maple.gg 캐릭터 정보창

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 존재하는 캐릭터인지 확인
            identifier = soup.find_all(self.identify_character)

            if identifier == []:
                print("검색결과가 없습니다.")
                await interaction.response.send_message(nickname + '님의 캐릭터 정보는 존재하지 않는 것 같아요!')
            else:
                if self.identify_info(soup) == None:
                    print("시드 기록이 없습니다.")
                    await interaction.response.send_message(nickname + '님은 더시드를 한 적이 없는 것 같아요!')
                else:
                    # 정보 크롤링
                    world = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > h3 > img')['alt']
                    job = soup.select_one(
                        '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)').get_text()
                    guild = soup.select_one(
                        '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div.col-lg-2.col-md-4.col-sm-4.col-12')
                    guild = guild.get_text().split()
                    guild = guild[1]
                    character_img_url = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img')['src']
                    urllib.request.urlretrieve(character_img_url, "character.png")
                    floor = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(2) > section > div > div > div > h1').get_text().replace('\n', '')
                    time = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(2) > section > div > div > div > small').get_text()
                    date = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(2) > section > footer > div.user-summary-date > span').get_text()

                    # 출력 테스트
                    print(f"월드: {world}")
                    print(f"층수: {floor}")
                    print(f"시간: {time}")
                    print(f"{date}")

                    # 임베드 변수
                    embed_title = nickname
                    embed_description = world + " / " + job
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
                            embed = discord.Embed(title=embed_title, url=url, description=embed_description,color=discord.Color.teal())
                    elif world == "리부트2":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=discord.Color.teal())
                    # 일반섭은 주황색
                    else:
                        # 제작자 1인 길드 소속 캐릭터면 루미나 옐로우색
                        if guild == "루미나" and world == "크로아":
                            embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0xE2E276)
                        else:
                            embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=discord.Color.orange())
                    embed.set_thumbnail(url="attachment://char.png")
                    embed.add_field(name="", value="", inline=False)
                    embed.add_field(name="달성 층", value=floor, inline=True)
                    embed.add_field(name="", value="", inline=True)
                    embed.add_field(name="소요 시간", value=time, inline=True)
                    embed.add_field(name="", value="", inline=False)
                    embed.set_footer(text=date)


                    await interaction.response.send_message(nickname + '님의 더시드 최고기록 정보를 불러왔어요!', embed=embed, file=char_img)
        else:
            print(response.status_code)


async def setup(bot):
    await bot.add_cog(Seed(bot))