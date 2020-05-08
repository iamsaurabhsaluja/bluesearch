import discord

from SearchGoogle import SearchGoogle

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
        search_results = gsearchengine.topResults(query, limit)
        return search_results

    """
    Method prepareResponse prepares the search query,
    it handles keyword understanding and distributes the message
    to the reque=ires methods
    """

    def prepareResponse( self, message ):

        """
        checking the user data
        """

        data = str(message.content)
        tokens = data.split(' ')
        query = data[len(tokens[0])+1:len(data)]

        if tokens[0].lower() == '!google':
            return self.search( query.strip() )

        if tokens[0].lower() == '!recent':
            return self.search( query.strip() )
