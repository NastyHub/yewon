import discord
import json
from discord.ext import commands, tasks
import random
from discord_components import DiscordComponents, ComponentsBot, Button

from discord.utils import MAX_ASYNCIO_SECONDS

##########################################################################
#generalrole = discord.utils.get(ctx.guild.roles, id=661454256251076613)
#logchannel = discord.utils.get(client.get_all_channels(), id = 753619980548833401)

#SERVER INFO
ownerid = 631441731350691850

chanwoo = 631441731350691850
yewon = 819734468465786891
saji = 785135229894524959
donggu = 543680309661663233
hanjae = 406822771524501516
mintchocolate = 434328592739074048
csticker = 864745666580316170
dohyun = 652531481767444498

##########################################################################

#USEFUL FUNCTIONS
##########################################################################

def checkidentity(supposeid):
    if int(supposeid) == chanwoo:
        return "chanwoo"
    elif int(supposeid) == yewon:
        return "yewon"
    elif int(supposeid) == saji:
        return "saji"
    elif int(supposeid) == donggu:
        return "donggu"
    elif int(supposeid) == hanjae:
        return "hanjae"
    elif int(supposeid) == mintchocolate:
        return "mint"
    elif int(supposeid) == csticker:
        return "csticker"
    elif int(supposeid) == dohyun:
        return "dohyun"
    else:
        return None

def sendrandom(providedlist, min, max):

    howmuchtosend = random.randint(min, max)
    sizeoflist = len(providedlist)
    i = 1
    returnlist = []

    while i <= howmuchtosend:
        i += 1
        thingtoadd = providedlist[random.randrange(0, sizeoflist)]

        returnlist.append(thingtoadd)
    
    return returnlist

def getlist(sendid):
    sendid = str(sendid)
    path = "ments/ments.json"

    with open(path) as f:
        jsondata = json.load(f)
        f.close()
    
    try:
        mylist = jsondata[sendid]
    except:
        mylist = None

    return mylist

class misc(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["8ball", "8볼", "질문"])
    async def question(self, ctx, *, question=None):
        if question == None:
            await ctx.send("질문을 입력해주세요.\n```?8볼 질문```\n*질문은 가급적 __예/아니오__ 답이 나올 수 있도록 해주세요*")
            return
        else:

            embed = discord.Embed(
                title = f"8볼 질문",
                description = f"받은 질문:\n```{question}```\n\n*질문은 가급적 __예/아니오__ 답이 나올 수 있도록 해주세요*\n\n**준비가 됐으면 8볼을 흔들어주세요!**",
                color = discord.Color.from_rgb(255,255,0)
            )
            embed.set_footer(text=f"{ctx.author.display_name}이 물어본 질문")
            embed.set_thumbnail(url="https://media.istockphoto.com/vectors/billiard-black-eight-vector-id614744860?k=20&m=614744860&s=612x612&w=0&h=hl4EtO9_2oEzndtohCGqwUt6sxtxlvUHyhJlZ2YvVRk=")

            msg = await ctx.send(
                embed=embed,
                components = [
                    Button(label = "🎱 흔들어주세요", custom_id = "8ballques", style=2)
                ],
            )

            interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "8ballques")
            await msg.edit(components = [])

            eightball = [
                "확실합니다",
                "그러겠네요",
                "의심의 여지도 없어요",
                "확실히 예라고 합니다",
                "그렇게 믿어도 돕니다",
                "제가보기에는 yes에요",
                "그럴 가능성이 높습니다",
                "전망이 좋네요",
                "예",
                "표지판은 예라고 가르킵니다",
                "흐랏한 답장이에요",
                "나중에 다시 요청하세요",
                "지금 말 안 해주는 게 낫겠네요",
                "지금은 예측할 수 없어요",
                "집중하고 다시 물어보세요",
                "기대도 하지 마세요",
                "제 대답은 아니오",
                "제 정보에 의하면 아닙니다",
                "전망이 그렇게 좋지는 않네요",
                "매우 의심스러워요"
            ]
            #shuffle the list eightball
            random.shuffle(eightball)
            #get the first element of the list
            result = eightball[0]

            newembed = discord.Embed(
                title = f"{ctx.author.display_name}#{ctx.author.discriminator}",
                description = f"제 대답:\n```{result}```",
                color = discord.Color.from_rgb(0,255,0)
            )
            newembed.set_footer(text=f"{ctx.author.display_name}이/가 물어본 질문")
            newembed.set_thumbnail(url="https://media.istockphoto.com/vectors/billiard-black-eight-vector-id614744860?k=20&m=614744860&s=612x612&w=0&h=hl4EtO9_2oEzndtohCGqwUt6sxtxlvUHyhJlZ2YvVRk=")

            await interaction.edit_origin(embed = newembed, content=interaction.user.mention)


def setup(client):
    client.add_cog(misc(client))