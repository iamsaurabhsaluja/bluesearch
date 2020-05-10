import os

import discord
import random
from dotenv import load_dotenv
import environ
import asyncio
import threading

from threading import Thread
from datetime import datetime

from discordsearch.services.StorageService import StorageService

class ProcessThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.started = datetime.now()

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        from discordsearch.services import initiateEngine

class ViewService:

    def startEngine( self ):
        service = StorageService()
        if service.getStartFlag():
            return;
        import pdb; pdb.set_trace()

        my_thread = ProcessThread("DiscordThread")
        my_thread.start()

        service.stopStartFlag()
