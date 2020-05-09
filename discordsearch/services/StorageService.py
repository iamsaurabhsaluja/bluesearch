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
from discordsearch.models import Keywords

class StorageService:

    def addToMessages( self, message, sender_id ):
        message = Messages( message = message, sender_id = sender_id )
        message.save()

        return message

    def addToKeywords( self, message, keyword ):
        keywork = Keywords( keyword = keyword, message = message )
        keywork.save()

        return keywork

    def getMessagesByKeyword( self, keyword ):
        Keywords = Keywords.objects.filter( Keyword = Keyword )
        return Keywords
