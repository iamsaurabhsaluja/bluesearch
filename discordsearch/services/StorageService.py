from discordsearch.models import Messages
from django.conf import settings

"""
import argparse
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesearch.settings')
import django
django.setup()
"""
from discordsearch.models import Messages

class StorageService:

    def store( self, message, sender_name ):
        message = Messages( message = message, sender_name = sender_name )
        message.save()
        print('added')
