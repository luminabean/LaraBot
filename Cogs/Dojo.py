import discord, asyncio, requests, urllib.request
from discord.ext import commands
from bs4 import BeautifulSoup

# 보스 정보
party_boss = {28: "3카룻, 노멀 시그너스",
              30: "하드 매그너스",
              31: "[최소]카오스 벨룸",
              34: "카오스 벨룸",
              35: "[소수]카오스 파풀라투스",
              36: "[최소]노멀 스우",
              38: "[최소]노멀 데미안",
              40: "[최소]노멀 가엔슬",
              42: "[소수]노멀 스우, 노멀 데미안 / 노멀 가엔슬",
              43: "[소수]노멀 가엔슬 / 이지 루시드 / [최소]이지 윌",
              44: "[소수]노멀 가엔슬 / 이지 윌 / [최소]노멀 루시드",
              45: "[소수]이지 루시드, 이지 윌, 노멀 가엔슬",
              46: "노멀 루시드 / [최소]노멀 윌",
              47: "노멀 윌 / [최소]노멀 더스크",
              48: "노멀 더스크 / [최소]노멀 듄켈, 하드 스우, 하드 데미안",
              49: "하드 스우, 하드 데미안 / [최소]하드 루시드",
              50: "노멀 듄켈, 하드 루시드 / [최소]노멀 진 힐라, 하드 윌",
              51: "노멀 진 힐라, 하드 윌",
              53: "[최소]카오스 더스크, 하드 진 힐라, 카오스 가엔슬",
              54: "카오스 더스크, 하드 진 힐라, 카오스 가엔슬",
              55: "[최소]하드 듄켈",
              56: "하드 듄켈",
              57: "[최소]하드 검은 마법사",
              58: "하드 검은 마법사",
              59: "[최소]하드 세렌",
              61: "[AUT 200]하드 세렌",
              64: "[AUT 180]하드 세렌",
              67: "[AUT 160]하드 세렌"}
solo_boss = {20: "이지 시그너스",
             28: "하드 힐라",
             32: "노멀 시그너스",
             33: "3카룻",
             35: "[최소]하드 매그너스",
             36: "카오스 벨룸, 하드 매그너스",
             41: "[최소]카오스 파풀라투스",
             42: "카오스 파풀라투스 / [최소]노멀 스우, 노멀 데미안",
             43: "노멀 스우",
             44: "노멀 데미안",
             46: "[최소]노멀 가엔슬",
             47: "[최소]이지 루시드, 노멀 가엔슬",
             48: "이지 루시드, 노멀 가엔슬 / [최소]이지 윌, 노멀 루시드",
             49: "이지 윌 / [최소]노멀 윌",
             50: "노멀 루시드, 노멀 윌 / [최소]노멀 더스크, 노멀 듄켈",
             51: "노멀 더스크 / [최소]하드 스우",
             52: "하드 스우",
             53: "[최소]하드 데미안",
             54: "노멀 듄켈, 하드 스우, 하드 데미안 / [최소]노멀 진 힐라",
             55: "노멀 진 힐라",
             56: "[최소]하드 윌",
             58: "하드 윌 / [최소]하드 듄켈",
             59: "[최소]하드 루시드, 카오스 더스크, 하드 진 힐라",
             60: "하드 진 힐라, 하드 듄켈 / [최소]카오스 가엔슬",
             61: "카오스 더스크",
             62: "카오스 가엔슬",
             67: "[최소]하드 검은 마법사",
             70: "하드 검은 마법사"}

class Dojo(commands.Cog, name="무릉도장"):
    def __init__(self, bot):
        self.bot = bot


    # 캐릭터가 존재하는지 확인한다
    def identify_character(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'user-summary-list'라는 클래스가 존재하는가?
            if class_name.startswith('user-summary-list') or class_name.startswith('user-summary-no-data'):
                return name


    # 기록이 존재하는지 확인한다
    def identify_result(self, name):
        if name.attrs.get('class'):
            class_name = name.attrs.get('class')[0]
            # 'user-summary-no-data'라는 클래스가 존재하는가?
            if class_name.startswith('user-summary-no-data'):
                return name


    @commands.command(name="무릉")
    async def dojo(self, ctx, nickname):
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
                identifier = soup.find_all(self.identify_result)

                if identifier != []:
                    print("무릉 기록이 없습니다.")
                    await ctx.send(nickname + '님은 무릉을 친 적이 없는 것 같아요!')
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
                    floor = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > div > div > div > h1').get_text().replace('\n', '')
                    time = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > div > div > div > small').get_text()
                    date = soup.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1) > section > footer > div.user-summary-date > span').get_text()

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
                    embed.add_field(name="", value="", inline=False)
                    embed.add_field(name="달성 층", value=floor, inline=True)
                    embed.add_field(name="", value="", inline=True)
                    embed.add_field(name="소요 시간", value=time, inline=True)
                    embed.add_field(name="", value="", inline=False)

                    if int(floor[:-1]) in party_boss.keys() and int(floor[:-1]) in solo_boss.keys():
                        embed.add_field(name="추천 보스", value="파티격: " + party_boss[int(floor[:-1])] + "\n" + "솔로격: " + solo_boss[int(floor[:-1])])
                    elif int(floor[:-1]) in party_boss.keys():
                        embed.add_field(name="추천 보스", value="파티격: " + party_boss[int(floor[:-1])] + "\n")
                    elif int(floor[:-1]) in solo_boss.keys():
                        embed.add_field(name="추천 보스", value="솔로격: " + solo_boss[int(floor[:-1])] + "\n")
                    embed.add_field(name="", value="", inline=False)
                    embed.set_footer(text=date + "\n추천 보스 정보는 정확하지 않을 수도 있습니다.")


                    await ctx.send(nickname + '님의 무릉도장 최고기록 정보를 불러왔어요!')
                    await ctx.channel.send(embed=embed, file=char_img)
        else:
            print(response.status_code)


async def setup(bot):
    await bot.add_cog(Dojo(bot))