import discord
import os
import json
from discord.ext import commands, tasks
import time
import asyncio
import random

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

class ments(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["테스트"])
    async def test(self, ctx):
        checkme = checkidentity(ctx.author.id)
        #await ctx.message.delete()

        if ctx.author.id == 434328592739074048:
            await ctx.send('...나는 모구모구')
            await ctx.send(file=discord.File('image/mogumogu.jpg'))
        else:
            grablist = getlist(ctx.author.id)

            if grablist == None:
                await ctx.send("아직 너는 잘 모르겠는데..")
            else:
                herelist = sendrandom(grablist, 1, 1)
                for i in herelist:
                    await ctx.send(i)

    @commands.command()
    async def joinvc(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.message.delete()
            channel = ctx.author.voice.channel

            await channel.connect()

    @commands.command()
    async def leavevc(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.message.delete()
            await ctx.voice_client.disconnect()

    @commands.command()
    async def sendjson(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.author.send(file=discord.File('ments/ments.json'))

    @commands.command(aliases=["전송"])
    async def dm(self, ctx, target: discord.Member, *, message):
        await ctx.message.delete()

        embed = discord.Embed(
            title = f"📨 메세지가 도착했습니다!",
            description = f"{message}\n\n```답장해도 보내지지 않으니 직접 그 사람에게 말하세용```명령어: `?전송 @유저 메세지 내용`",
            color = discord.Color.from_rgb(255,105,180)
        )
        embed.set_footer(text=f"{ctx.author.name}님이 보낸 메세지")
        try:
            await target.send(embed=embed)
        except:
            await ctx.send(f"{target.mention}, 도착한 메세지가 있었지만 디엠 수신 기능이 꺼져있어 보내지 못하였습니다.")   

        #find channel with id = 879895499338039301
        channel = discord.utils.get(ctx.guild.channels, id = 879895499338039301)
        await channel.send(embed=embed)
                 

def setup(client):
    client.add_cog(ments(client))