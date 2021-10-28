import discord
import os
import json
from discord.ext import commands, tasks
import time
import asyncio
import random
import sqlite3

from discord.utils import MAX_ASYNCIO_SECONDS

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

client = commands.Bot(command_prefix = '?', intents=intents)
client.remove_command('help')

conn = sqlite3.connect("database.db")
c = conn.cursor()

##########################################################################
#generalrole = discord.utils.get(ctx.guild.roles, id=661454256251076613)
#logchannel = discord.utils.get(client.get_all_channels(), id = 753619980548833401)

#SERVER INFO
ownerid = 631441731350691850

##########################################################################

#USEFUL FUNCTIONS
##########################################################################

class money(commands.Cog):

    def __init__(self, client):
        self.client = client


    @client.command(aliases=["계좌생성"])
    async def makeaccount(self, ctx):
        await ctx.send("ok.")

def setup(client):
    client.add_cog(money(client))