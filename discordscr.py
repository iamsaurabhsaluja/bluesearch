# bot.py
import os

import discord
import random
from dotenv import load_dotenv
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

GUILD=env('GUILD')
TOKEN=env('TOKEN')

#load_dotenv('.env')
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    members = '\n - '.join([member.name for member in guild.members])
    print(members)

#bot = DiscordBot()
client.run(TOKEN)
