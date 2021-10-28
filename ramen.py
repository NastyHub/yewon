import discord
from discord.ext import commands, tasks
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

with open("token.txt") as f:
    bottoken = f.read()
    f.close()

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

##########################################################################
@client.event
async def on_ready():
    game = discord.Game(name = "상원 20818 짜파게티")
    await client.change_presence(activity = game)

    print("Ready to Run")

##########################################################################

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.command()
async def load(ctx, name):
    if ctx.author.id == ownerid:
        client.load_extension(f"cogs.{name}")
        await ctx.send("Done!")

@client.command()
async def unload(ctx, name):
    if ctx.author.id == ownerid:
        client.unload_extension(f"cogs.{name}")
        await ctx.send("Done!")


client.run(bottoken)