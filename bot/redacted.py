import os
import discord
import asyncio
from datetime import datetime

from dotenv import load_dotenv
from discord.ext import commands, tasks

import database
from database import Database 

from wow import *
from util import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASS = os.getenv("POSTGRES_PASSWORD")
DATABASE_NAME = os.getenv("POSTGRES_DB")
DATABASE_HOST = os.getenv("POSTGRES_HOST")
DATABASE_PORT = os.getenv("POSTGRES_PORT")

bot = commands.Bot(command_prefix = "!r-")

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

@bot.command( name = "add-character", help = "Add WoW character. Usage: !r-add-character <CharacterName>")
async def add_character(ctx, character_name: str):
    character = await get_character(character_name)

    if character == "not_found":
        await ctx.send("Character not found!")
    
    else:
        #print(character, flush = True)
        
        class_data = await class_details(character["class"])
        class_colour = class_data["colour"]
        class_name = class_data["name"]
        
        msg = discord.Embed(
            title = "%s" % (character["name"]),
            colour = discord.Colour(class_colour),
            description = "%s, %s - %s" % (character["level"], class_name, character["spec"])
        )
        msg.set_thumbnail(
            url = character["thumbnail"]
        )
        msg.add_field(
            name = "Character",
            value = "**Name:** %s\n**Item Level:** %s"
            % (character["name"], character["ilvl"]),
            inline = True
        )
        msg.add_field(
            name = "Who Sent?",
            value = ctx.author.id,
            inline = True
        )

    db = Database()
    await db.connect(DATABASE_USER, DATABASE_PASS, DATABASE_HOST, DATABASE_PORT, DATABASE_NAME)
    await db.set_cursor(False)
    result = await db.add_character(ctx.author.id, character)
    await db.exit()

    if result == "character_exists":
        await ctx.channel.send("Character already exists in database!")
    else:
        await ctx.channel.send(embed=msg)
        await ctx.channel.send("Is this your character?")

@bot.command( name = "confirm-character", help = "Add WoW charcter. Usage: !r-confirm-character <CharacterName> <y/n>")
async def confirm_character(ctx, character_name: str, confirm: bool):
    if confirm == True:
        await ctx.channel.send("Adding character to database.")
    else:
        await ctx.channel.send("Retry using !r-add-character again. If problem persists contact an admin.")

#@bot.command( name = "get-character", help = "Add WoW charcter. Usage: !r-get-character <CharacterName>")
async def get_character(character_name: str):
    return await get_character_info(character_name.lower())


@bot.command( name = "test", help = "")
async def test_command(ctx):
    print("Channel Command", flush = True)
    channel = discord.utils.get(bot.get_all_channels(), name = "dead")

    #channel = client.get_channel(12324234183172)
    await channel.send("hello")

    print(channel, flush = True)

# Run Commands every 24 hours on WoW Daily reset
@tasks.loop(minutes=1.0)
async def task(self):
    channel = discord.utils.get(bot.get_all_channels(), name = "news")
    
    if datetime.now().hour == 0:
        print("hello", flush = True)
        await channel.send("Command ran successfully")

bot.run(TOKEN)