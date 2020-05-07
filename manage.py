#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
import discord
import random
import subprocess
import threading

from dotenv import load_dotenv

#from discort import DiscordBot as bot

GUILD=''
TOKEN=''

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
#client.run(TOKEN)

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesearch.settings')

def start():
    #client.run(TOKEN)
    subprocess.Popen(['python','discordscr.py'])

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesearch.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    start()
    main()
