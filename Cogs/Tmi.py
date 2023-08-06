import discord, asyncio, random
from discord import app_commands
from discord.ext import commands
from discord import Interaction

class Tmi(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot


    @app_commands.command(name="tmi", description="라라봇이 쓸모없는 TMI 정보를 알려줘요.")
    async def tmi(self, interaction: Interaction):
        rand = random.randrange(1, 46)
        tmi_msg = ""
        tmi_ps = ""

        if rand == 1:
            tmi_msg = "듀얼블레이드의 5차스킬 강화 코어 개수는 무려 16개나 된다네요!"
            tmi_ps = "하지만 유효 코어는 6개 뿐..."
        if rand == 2:
            tmi_msg = "캐논슈터의 5차스킬 강화 코어 개수는 무려 16개나 된다네요!"
            tmi_ps = "하지만 유효 코어는 6개 뿐..."
        if rand == 3:
            tmi_msg = "마이스터빌과 자유시장의 창고지기는 아이템을 보관하거나 찾을 때 메소를 더 많이 받아요!"
            tmi_ps = "보관할 때는 500메소, 찾을 때는 1,000메소!."
        if rand == 4:
            tmi_msg = "나이트워커의 하이퍼스킬인 도미니언은 전용 BGM을 가진 최초의 스킬이에요."
        if rand == 5:
            tmi_msg = "루미너스의 진리의 문은 스킬 보이스가 존재하는 최초의 5차스킬이에요."
        if rand == 6:
            tmi_msg = "팬텀의 5차 스킬인 조커는 뽑은 카드에 따라서 스킬 보이스가 달라져요."
        if rand == 7:
            tmi_msg = "미하일은 이론상 인생의 3분의 2가 무적인 상태로 살 수 있어요."
            tmi_ps = "로얄 가드 쿨타임은 6초인데 무적 시간은 4초라니!"
        if rand == 8:
            tmi_msg = "라라봇의 개발자는 라라 250을 찍은 기념으로 양꼬치를 먹었다고 해요."
            tmi_ps = "너무해 ㅜㅜ"
        if rand == 9:
            tmi_msg = "라라봇에게 바보라고 하면 10%의 확률로 라라봇이 다른 반응을 보인다고 해요!"
            tmi_ps = "라라는 바보가 아니라구요 ㅜㅜ"
        if rand == 10:
            tmi_msg = "140제 튜너의 이름은 우트가르트 리스트레인트와 라이온하트 리스트레인트에요."
            tmi_ps = "[우르가르트 리스트레인트]링"
        if rand == 11:
            tmi_msg = "스우는 스킬을 사용할 때 말을 하지 않는 것 같지만, 사실 말을 하고 있어요."
            tmi_ps = "25%의 확률로 스킬 보이스가 나오지만, 소리가 작기 때문에 잘 안 들려요."
        if rand == 12:
            tmi_msg = "13채널 루타비스에는 왜 만렙 의자가 유독 많이 보일까요?"
            tmi_ps = "보스 매칭 시스템이 존재했을 당시, 13채널이 루타비스 보스의 매칭 채널이었기 때문이에요."
        if rand == 13:
            tmi_msg = "미하일은 보조무기가 없어도 로얄 가드를 사용할 수 있어요!"
            tmi_ps = "방패가 없는데 방패로 막을 수가 있나...?"
        if rand == 14:
            tmi_msg = "아델의 주력기인 디바이드는 스킬 이펙트가 3종류나 존재해요."
            tmi_ps = "하지만 남에게는 한 가지로 고정되어 보여요."
        if rand == 15:
            tmi_msg = "소울마스터의 주력기인 루나 디바이드 VI는 스킬 이펙트가 3종류나 존재해요."
            tmi_ps = "달을 베는 방향이 달라져요!"
        if rand == 16:
            tmi_msg = "우르스 격파로 받을 수 있는 메소는 캐릭터의 레벨과 등급에 비례해요."
            tmi_ps = "200레벨 이상 기준, S등급을 받았다면 13,821 x (캐릭터의 레벨)만큼 메소를 받을 수 있어요."
        if rand == 17:
            tmi_msg = "슬라임은 사과향이 나기 때문에 요리 재료로도 쓰인다고 해요."
            tmi_ps = "탕윤의 요리교실 파티퀘스트에서는 실제로 슬라임푸딩을 만들어 볼 수 있어요."
        if rand == 18:
            tmi_msg = "오르비스의 표지판은 헬라어로 쓰여져 있어요."
        if rand == 19:
            tmi_msg = "다섯 영웅의 이름의 앞글자를 모으면 MAPLE이 돼요."
            tmi_ps = "메르세데스(M) 아란(A) 팬텀(P) 루미너스(L) 에반(E)"
        if rand == 20:
            tmi_msg = "모험가와 친구들 이름의 앞글자를 모으면 STORY가 돼요."
            tmi_ps = "슈가(S) 테스(T) 올리비아(O) 론도(R) 그리고... 당신(Y)"
        if rand == 21:
            tmi_msg = "19주년 이벤트맵(메이플 모멘트리)의 NPC들의 이름은 빅토리아 아일랜드의 마을에서 유래되었어요."
            tmi_ps = "리스(리스항구) 엘리(엘리니아) 케닐(커닝시티) 리페(페리온) 헤르만(헤네시스) 티리스(노틸러스)"
        if rand == 22:
            tmi_msg = "20주년 이벤트맵(메이프릴 아일랜드) NPC의 이름의 앞글자를 모으면 MAPLE이 돼요."
            tmi_ps = "마리엘라(M) 에이프리샤(A) 플라나(P) 레오나(L) 엠마(E)"
        if rand == 23:
            tmi_msg = "20주년 이벤트맵(메이프릴 아일랜드)의 NPC인 아멜리 포츠는 Maplestory의 애너그램으로 이루어진 이름이에요."
            tmi_ps = "Maplestory -> Amely Ports"
        if rand == 24:
            tmi_msg = "최초의 메가버닝 이벤트는 2014년 12월, MIB 업데이트때 시작되었어요."
            tmi_ps = "박준형과 장동민이 광고 모델(이벤트 NPC)로 나왔다고 해요."
        if rand == 25:
            tmi_msg = "메이플스토리에는 놀랍게도, 유재석의 NPC 데이터가 존재해요."
            tmi_ps = "2015년 1월 네네치킨 콜라보 당시 '유점장' 이라는 이름의 NPC로 존재했어요. 심지어 유점장 NPC 근처에 가면 네네치킨 광고 음악이 나왔다고 하네요!"
        if rand == 26:
            tmi_msg = "최초의 테라버닝 이벤트는 2018년 6월, 검은마법사 업데이트때 시작되었어요."
        if rand == 27:
            tmi_msg = "어드벤처 업데이트 당시, 테라버닝 달성 보상으로 영구 루타비스 세트를 지급한 적이 있었어요."
            tmi_ps = "지금은 90일 기간제로 주고 있어요."
        if rand == 28:
            tmi_msg = "셀라스(Sellas)라는 글자는 180도 돌려서 봐도 셀라스로 보여요."
        if rand == 29:
            tmi_msg = "엘리니아의 요정들은 고맙지만 사양을 하고 싶을 때 메롱을 한다고 해요."
        if rand == 30:
            tmi_msg = "헤네시스에는 유치원이 존재해요!"
        if rand == 31:
            tmi_msg = "아랫마을 테마던전 퀘스트를 깼다면, 아랫마을에 있는 측간에서 볼일을 볼 수 있게 돼요."
            tmi_ps = "랜덤 한 개의 성향 경험치가 5 올라요. 단, 하루에 한 번만 볼일을 볼 수 있다고 해요."
        if rand == 32:
            tmi_msg = "주황버섯은 점프를 하지 않으면 버섯집으로 변한다고 해요."
            tmi_ps = "던전 블래스트의 좀비 머쉬맘: 집이 되긴 싫어!"
        if rand == 33:
            tmi_msg = "엑스텀프의 머리에 도끼가 있는 이유는 한 소녀에 대한 그리움 때문이라고 해요."
            tmi_ps = "강해지고 싶어서 머리에 도끼를 찍은 게 아니라고요!"
        if rand == 34:
            tmi_msg = "물 도둑이 물을 훔치는 이유는 벨에게 보습제를 만들어 주기 위해서래요!"
        if rand == 35:
            tmi_msg = "옛날에는 달팽이의 껍질이 있어야 달팽이 세마리 스킬을 쓸 수 있었다고 해요."
        if rand == 36:
            tmi_msg = "월묘의 떡은 타오르는 돌(파이어 믹스 골렘)와 서전아이의 꼬리(서전아이)로 만들어졌다고 해요."
        if rand == 37:
            tmi_msg = "핑크빈은 엔젤릭버스터의 노래를 즐겨듣는다고 해요."
            tmi_ps = "내 맘에 핑크가 버블버블~♪"
        if rand == 38:
            tmi_msg = "옛날에는 사망한 상태에서도 전투의 흐름 링크스킬이 발동되었다고 해요."
            tmi_ps = "...하지만 버그 악용으로 인해 막혔다고 해요."
        if rand == 39:
            tmi_msg = "해적 직업 캐릭터는 무기가 없어도 공격을 할 수 있다고 해요."
        if rand == 40:
            tmi_msg = "엘리트 몬스터는 머리에 떠있는 검의 색에 따라서 체력이 달라져요."
            tmi_ps = "노란색이면 일반 몬스터의 15배, 주황색이면 20배, 빨간색이면 30배라고 해요."
        if rand == 41:
            tmi_msg = "메이플스토리는 세계 최초의 2D 횡스크롤 MMORPG 게임이에요."
        if rand == 42:
            tmi_msg = "메이플스토리는 세계 최초로 가챠 시스템을 도입한 게임이에요."
            tmi_ps = "정확히는 JMS(일본 메이플스토리)지만요..."
        if rand == 43:
            tmi_msg = "메이플스토리는 반지의 제왕을 모티브로 만들어졌다고 해요!"
        if rand == 44:
            tmi_msg = "루타비스는 이상한 나라의 앨리스를 모티브로 만들어졌다고 해요!"
        if rand == 45:
            tmi_msg = "더 시드는 오즈의 마법사를 모티브로 만들어졌다고 해요!"

        print(f"rand: {rand}")
        print(f"msg: {tmi_msg}")


        # 임베드 변수
        embed_title = "라라의 TMI 쇼!"
        embed_description = "#" + str(rand)

        # 임베드 양식
        embed = discord.Embed(title=embed_title, description=embed_description, color=discord.Color.yellow())
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name=tmi_msg, value=tmi_ps, inline=True)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Tmi(bot))
