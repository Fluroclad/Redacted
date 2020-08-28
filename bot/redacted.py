import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

from wow import *
from util import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix = "!r-")

@bot.command( name = "test", help = "A test command.")
async def test_com(ctx):
    response = "This is a testing command has been updated."
    await ctx.send(response)

@bot.command( name = "curve", help = "Returns those who have curve and don't for current raid tier.")
async def curve(ctx):
    response = "Return Curve. (Maybe add curve roll to those who have obtained it)"
    await ctx.send(response)

@bot.command( name = "ce", help = "Returns those who have cutting edge and don't for current raid tier.")
async def cutting_edge(ctx):
    response = "lol u think we ever getting cutting edge."
    await ctx.send(response)

@bot.command( name = "update-characters", help = "Update all characters attached to your discord account.")
async def update_characters(ctx):
    response = "Update main and alt characters."
    await ctx.send(response)

@bot.command( name = "get-character", help = "Add WoW charcter. Usage: !r-add-character <CharacterName>")
async def get_character(ctx, character_name: str):

    character = await get_character_info(character_name.lower())
    
    if character == "not_found":
        await ctx.send("Character not found!")
    
    else:
        print(character, flush = True)

        class_data = await class_details(character["class"])
        class_colour = class_data["colour"]
        class_name = class_data["name"]
        
        msg = discord.Embed(
            title = "%s" % (character["name"]),
            colour = discord.Colour(class_colour),
            description = "%s, %s - %s" % (character["level"], class_name, character["spec"])
        )
        msg.add_field(
            name = "Character",
            value = "**'Name':** '%s'\n**'Item Level':** '%s'"
            % (character["name"], character["ilvl"]),
            inline = True
        )

        await ctx.channel.send(embed=msg)

bot.run(TOKEN)