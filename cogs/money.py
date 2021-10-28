import discord
from discord.ext import commands, tasks
import asyncio
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

def getbanklist():
    wow = c.execute("""SELECT bankname FROM banklist WHERE auth_key = 123""").fetchall()
    banknamelist = []
    for i in wow:
        banknamelist.append(i[0])
    return banknamelist


##########################################################################

class money(commands.Cog):

    def __init__(self, client):
        self.client = client


    @client.command(aliases=["계좌생성"])
    async def makeaccount(self, ctx):
        banknamelist = getbanklist()

        gethowmany = len(banknamelist)

        result = "은행종류:"
        upcomingnumber = 1

        for i in banknamelist:
            result += f"\n{upcomingnumber}: {i}"
            upcomingnumber += 1
        
        emojilist = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "❌"]

        message = await ctx.reply(result)
        i = 0

        while i <= gethowmany-1:
            await message.add_reaction(emojilist[i])
            i += 1
        await message.add_reaction(emojilist[5])

    @client.command(aliases=["은행정보"])
    async def bankinfo(self, ctx, bankname=None):
        print(",")

def setup(client):
    client.add_cog(money(client))