import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix = "!r-")

@bot.command( name = "test", help = "A test command.")
async def test_com(ctx):
    response = "This is a testing command has been updated."
    await ctx.send(response)

bot.run(TOKEN)