from django.conf import settings

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
        keywords = Keywords.objects.filter( keyword = keyword ).order_by('-created_time')[:20]
        return keywords

    def getMessageCount( self, message ):
        messages = Messages.objects.filter( message = message )
        return len(messages)
