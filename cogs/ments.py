import discord
import os
import json
from discord.ext import commands, tasks
import time
import asyncio
import random

from discord.utils import MAX_ASYNCIO_SECONDS

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

client = commands.Bot(command_prefix = '?', intents=intents)
client.remove_command('help')

##########################################################################
#generalrole = discord.utils.get(ctx.guild.roles, id=661454256251076613)
#logchannel = discord.utils.get(client.get_all_channels(), id = 753619980548833401)

#SERVER INFO
ownerid = 631441731350691850

members = {
    631441731350691850: "chanwoo",
    819734468465786891: "yewon",
    785135229894524959: "saji",
    543680309661663233: "donggu",
    406822771524501516: "hanjae",
    434328592739074048: "mintchocolate",
    864745666580316170: "csticker",
    652531481767444498: "dohyun",
    421557594625409024: "valentine",
}
##########################################################################

#USEFUL FUNCTIONS
##########################################################################

def checkidentity(supposeid: int):
    """ checks identity of caller

    Args:
        supposeid (int): [ctx.author.id]

    Returns:
        [None]: [nothing]
    """
    if supposeid in members:
        return members[supposeid]
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


    @client.command(aliases=["테스트"])
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

    @client.command()
    async def joinvc(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.message.delete()
            channel = ctx.author.voice.channel

            await channel.connect()

    @client.command()
    async def leavevc(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.message.delete()
            await ctx.voice_client.disconnect()

    @client.command()
    async def sendjson(self, ctx):
        if ctx.author.id == ownerid:
            await ctx.author.send(file=discord.File('ments/ments.json'))

def setup(client):
    client.add_cog(ments(client))