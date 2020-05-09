import discord

from discordsearch.services.SearchGoogle import SearchGoogle
from discordsearch.services.StorageService import StorageService
from discordsearch.services.CoreService import CoreService

class AnsweringBot:

    """
    Method search access SearchGoogle custom class,
    which actually calls google api to get results

    Configuration:

    Here option is given to specify number of links
    to be displayed on screen
    """

    def search( self, query ):
        limit = 5
        gsearchengine = SearchGoogle()
        search_results = ['success'] #gsearchengine.topResults(query, limit)
        return search_results

    """
    Method storeSearch creates the search history
    """

    def storeSearch( self, message, sender_id ):
        core = CoreService()
        core.track( message, sender_id )

    def coreSearch( self, query ):
        words = query.split(' ')
        core = CoreService()
        return core.coreSearch( words )

    """
    Method prepareResponse prepares the search query,
    it handles keyword understanding and distributes the message
    to the required method
    """

    def prepareResponse( self, message, sender_id ):

        """
        checking the user data
        """

        tokens = message.split(' ')
        query = message[len(tokens[0])+1:]

        if tokens[0].lower() == '!google':
            response = self.search( query.strip() )
            self.storeSearch( query, sender_id )
            return response

        if tokens[0].lower() == '!recent':
            return self.coreSearch( query )
