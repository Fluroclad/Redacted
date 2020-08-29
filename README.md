# Redacted Guild Discord Bot
Custom Discord Bot built for the Redacted-Silvermoon Guild.

# Getting Started
You will be needing to get API and OAUTH tokens from Discord and Blizzard to start using this bot.

* https://discord.com/developers/applications
* https://develop.battle.net/access/

Follow their respective documents to get started with connecting to blizzard api and adding the discord bot to a server.

NOTE: Signing up to Blizzard API mark the checkbox "I do not have a service URL for this client".

I am currently testing the bot out in https://discord.gg/65aWUuW. Message me Fluroclad#4235 on discord if you need access to do testing although it is probably easier if you have your own discord server to play around with the bot in. If you do come to this server make sure you change the command prefix to something unique in redacted.py, here is the line for reference.

```
bot = commands.Bot(command_prefix = "!r-")
```

To start using this bot once all the preliminaries are set up. Be in the project directory and use this command if running for the first time or making changes to the dependencies of the container.
```
docker-compose up -- build
```
Or builds with only changes to the application itself (bot/database)
```
docker-compose up
```

If you need to delete the database use this (Warning: it deletes the whole database data. There is no backup system for now)
```
rm ./database/data
```