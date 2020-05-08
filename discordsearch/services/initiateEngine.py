import os

import discord
import random
from dotenv import load_dotenv
import environ

from discordsearch.services.MessageHandler import MessageHandler

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

GUILD=env('GUILD')
TOKEN=env('TOKEN')

#initiating the client
client = discord.Client()

#This is called when any message comes in discord chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    bot_messages = MessageHandler.handle( message )

    for bot_message in bot_messages:
        await message.channel.send( bot_message )

#This is called when discord chat is ready
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    members = '\n - '.join([member.name for member in guild.members])
    print(members)

#booting up engine
client.run(TOKEN)
