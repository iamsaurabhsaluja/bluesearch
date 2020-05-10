import os

import discord
import random
from dotenv import load_dotenv
import environ
import asyncio
import threading
import sys

from discordsearch.services.MessageHandler import MessageHandler

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
#environ.Env.read_env()

GUILD=env('GUILD')
TOKEN=env('TOKEN')

#initiating the client
client = discord.Client()

print("reached client")
sys.stdout.flush()

async def start():
    print("starting client")
    sys.stdout.flush()

    await client.start(TOKEN) # use client.start instead of client.run

def run_it_forever(loop):
    loop.run_forever()

def init():
    asyncio.get_child_watcher() # I still don't know if I need this method. It works without it.

    loop = asyncio.get_event_loop()
    loop.create_task(start())

    thread = threading.Thread(target=run_it_forever, args=(loop,))
    thread.start()

"""
This runs from start method of manage.py
This implements on_message and on_ready functions of discord
on_message calls passes the message to MessageHandler
"""

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

print("starting init")
sys.stdout.flush()
init();
