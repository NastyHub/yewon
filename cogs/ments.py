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


    @commands.command(aliases=["?????????"])
    async def test(self, ctx):
        checkme = checkidentity(ctx.author.id)
        #await ctx.message.delete()

        if ctx.author.id == 434328592739074048:
            await ctx.send('...?????? ????????????')
            await ctx.send(file=discord.File('image/mogumogu.jpg'))
        else:
            grablist = getlist(ctx.author.id)

            if grablist == None:
                await ctx.send("?????? ?????? ??? ???????????????..")
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

    @commands.command(aliases=["??????"])
    async def dm(self, ctx, target: discord.Member, *, message):
        try:
            await ctx.message.delete()
        except:
            await ctx.send("??? ???????????? ???????????? ????????? ?????????")

        embed = discord.Embed(
            title = f"???? ???????????? ??????????????????!",
            description = f"```{message}```\n\n???????????? ???????????? ????????? ?????? ??? ???????????? ????????????\n?????????: `??????? @?????? ????????? ??????`",
            color = discord.Color.from_rgb(255,105,180)
        )
        embed.set_footer(text=f"{ctx.author.name}?????? ?????? ?????????")
        try:
            await target.send(embed=embed)
        except:
            await ctx.send(f"{target.mention}, ????????? ???????????? ???????????? ?????? ?????? ????????? ???????????? ????????? ??????????????????.")   

        #find a channel with an id 879895499338039301 from all the servers the bot is in
        channel = discord.utils.get(self.client.get_all_channels(), id = 879895499338039301)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(ments(client))