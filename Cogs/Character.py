import discord, asyncio, requests, urllib.request
from discord.ext import commands
from bs4 import BeautifulSoup


class Character(commands.Cog, name="유저"):
    def __init__(self, bot):
        self.bot = bot


    # 캐릭터가 존재하는지 확인한다
    def identify_character(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'user-summary-list'라는 클래스가 존재하는가?
            if class_name.startswith('user-summary-list'):
                return name


    @commands.command(name="정보")
    async def character(self, ctx, nickname):
        url = "https://maple.gg/u/" + nickname  # maple.gg 캐릭터 정보창

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 존재하는 캐릭터인지 확인
            identifier = soup.find_all(self.identify_character)

            if identifier == []:
                print("검색결과가 없습니다.")
                await ctx.send(nickname + '님의 정보는 존재하지 않는 것 같아요!')
            else:
                # 정보 크롤링
                world = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > h3 > img')['alt']
                world_img_url = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > h3 > img')['src']
                urllib.request.urlretrieve("https:" + world_img_url, "world.png")
                level_info = soup.select_one(
                    '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(1)')
                job = soup.select_one(
                    '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(2)')
                popularity = soup.select_one(
                    '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.user-summary > ul > li:nth-child(3)')
                popularity = popularity.get_text().split()
                popularity = popularity[1]
                guild = soup.select_one(
                    '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div.col-lg-2.col-md-4.col-sm-4.col-12')
                guild = guild.get_text().split()
                guild = guild[1]
                character_img_url = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img')['src']
                urllib.request.urlretrieve(character_img_url, "character.png")
                ranking = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(2) > span')
                ranking = ranking.get_text().replace(" ", "")
                ranking_world = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(3) > span')
                ranking_job =  soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(5) > span')
                ranking_job_world = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div:nth-child(4) > span')
                update_date = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.mt-2.text-right.clearfix > div > span')
                update_date = update_date.get_text().replace(" ", "")[9:]

                # 출력 테스트
                print(f"월드: {world}")
                print(f"레벨: {level_info.get_text()}")
                print(f"직업: {job.get_text()}")
                print(f"인기도: {popularity}")
                print(f"길드: {guild}")
                print(f"랭킹: {ranking} / {ranking_world.get_text()}")
                print(f"직업랭킹: {ranking_job.get_text()} / {ranking_job_world.get_text()}")
                print(f"마지막 업데이트: {update_date}")

                # 임베드 변수
                embed_title = nickname
                embed_description = world + " / " + job.get_text()
                char_img = discord.File("character.png", filename="char.png")
                level = level_info.get_text()

                # 임베드 양식
                # 제작자 캐릭터면 루미나 그린색
                if nickname == "탠루나" or nickname == "나방콩":
                    embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0x99E593)
                # 리부트는 청록색
                elif world == "리부트" or world == "리부트2":
                    # 제작자가 속한 길드의 유저라면 밝은 회색
                    if guild == "그리폰":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description,color=discord.Color.light_gray())
                    # 제작자 1인 길드 소속 캐릭터면 루미나 그린색
                    elif guild == "심포니":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0x99E593)
                    else:
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description,color=discord.Color.teal())
                # 일반섭은 주황색
                else:
                    # 제작자 1인 길드 소속 캐릭터면 루미나 옐로우색
                    if guild == "루미나" and world == "크로아":
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=0xE2E276)
                    else:
                        embed = discord.Embed(title=embed_title, url=url, description=embed_description, color=discord.Color.orange())
                embed.set_thumbnail(url="attachment://char.png")
                embed.add_field(name="", value="")
                embed.add_field(name="레벨", value=level, inline=False)
                embed.add_field(name="인기도", value=popularity, inline=True)
                embed.add_field(name="길드", value=guild, inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="종합랭킹", value=ranking.replace("\n", ""), inline=True)
                embed.add_field(name="월드랭킹", value=ranking_world.get_text(), inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="직업랭킹(전체)", value=ranking_job.get_text(), inline=True)
                embed.add_field(name="직업랭킹(월드)", value=ranking_job_world.get_text(), inline=True)
                embed.add_field(name="", value="", inline=True)
                embed.add_field(name="", value="")
                embed.set_footer(text="maple.gg 마지막 업데이트: " + update_date.lstrip())


                await ctx.send(nickname + '님의 정보를 불러왔어요!')
                await ctx.channel.send(embed=embed, file=char_img)
        else:
            print(response.status_code)


async def setup(bot):
    await bot.add_cog(Character(bot))