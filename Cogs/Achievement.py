import discord, asyncio, requests, urllib.request
from discord.ext import commands
from bs4 import BeautifulSoup


class Union(commands.Cog, name="유니온"):
    def __init__(self, bot):
        self.bot = bot


    # 캐릭터가 존재하는지 확인한다
    def identify_character(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'user-summary-list'라는 클래스가 존재하는가?
            if class_name.startswith('user-summary-list'):
                return name


    @commands.command(name="유니온")
    async def Union(self, ctx, nickname):
        url = "https://maple.gg/u/" + nickname  # maple.gg 캐릭터 정보창

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 존재하는 캐릭터인지 확인
            identifier = soup.find_all(self.identify_character)

            if identifier == []:
                print("검색결과가 없습니다.")
                await ctx.send(nickname + '님의 유니온 정보를 찾을 수 없어요!')
            else:
                # 정보 크롤링
                world = soup.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div > h3 > img')['alt']
                guild = soup.select_one(
                    '#user-profile > section > div.row.row-normal > div.col-lg-8 > div > div.row.row-normal.user-additional > div.col-lg-2.col-md-4.col-sm-4.col-12')
                guild = guild.get_text().split()
                guild = guild[1]
                rank_img_url = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(4) > section > div > div > img')['src']
                urllib.request.urlretrieve(rank_img_url, "rank.png")
                rank_name = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(4) > section > div > div > div').get_text()
                score = soup.select_one(
                    '#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(4) > section > div > div > span').get_text().split()[1]
                date = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(4) > section > footer > div.user-summary-date > span').get_text()

                # 출력 테스트
                print(f"월드: {world}")
                print(f"랭크: {rank_name}")
                print(f"업적 점수: {score}점")
                print(f"{date}")

                # 임베드 변수
                embed_title = rank_name
                embed_description = nickname + " / " + world
                rank_img = discord.File("rank.png", filename="rank.png")

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
                embed.set_thumbnail(url="attachment://rank.png")
                embed.add_field(name="", value="")
                embed.add_field(name="업적 점수", value=score, inline=False)
                embed.add_field(name="", value="")
                embed.set_footer(text=date)


                await ctx.send(nickname + '님의 업적 정보를 불러왔어요!')
                await ctx.channel.send(embed=embed, file=rank_img)
        else:
            print(response.status_code)


async def setup(bot):
    await bot.add_cog(Union(bot))