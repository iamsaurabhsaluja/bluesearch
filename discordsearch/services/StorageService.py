from django.conf import settings

from discordsearch.models import Messages
from discordsearch.models import Keywords
from discordsearch.models import Engine

class StorageService:

    def addToMessages( self, message, sender_id ):
        message = Messages( message = message, sender_id = sender_id )
        message.save()

        return message

    def addToKeywords( self, message, keyword, sender_id ):
        keywork = Keywords( keyword = keyword, message = message, sender_id = sender_id )
        keywork.save()

        return keywork

    def getKeywordsByWord( self, word, sender_id ):
        keywords = Keywords.objects.filter( keyword = word, sender_id = sender_id ).order_by('-created_time')[:20]
        return keywords

    def getMessageCount( self, message, sender_id ):
        messages = Messages.objects.filter( message = message, sender_id = sender_id )
        return len(messages)

    def getTopMessages( self, sender_id ):
        messages = Messages.objects.filter( sender_id = sender_id ).order_by('-created_time')[:20]
        return messages

    def startStartFlag( self ):
        if len(Engine.objects.all()) == 0:
            flag = Engine( started = 0 )
            flag.save()
        else:
            flag = Engine.objects.all()[0]
            flag.started = 0
            flag.save()

    def getStartFlag( self ):
        flag = Engine.objects.all()[0]
        return flag.started

    def stopStartFlag( self ):
        flag = Engine.objects.all()[0]
        flag.started = 1
        flag.save()
