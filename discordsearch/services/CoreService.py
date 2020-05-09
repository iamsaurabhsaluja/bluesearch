from discordsearch.services.StorageService import StorageService
from functools import cmp_to_key
import random
import concurrent.futures

class CoreService:

    """
    Method makeKeyworks is called by track to perform
    subwording task.
    For a search !Google game of thrones

    This breakes thrones into, thro, throne, one etc
    to make search better
    """
    def makeKeyworks( self, word, msg, sender_id ):
        length = len(word)
        N = length

        while N > 0:
            for i in range(0,length-N+1):
                subword = word[i:i+N]
                store_service = StorageService()
                store_service.addToKeywords( msg, subword, sender_id )

            N = N-1

    """
    Method track is called by prepareResponse of AnsweringBot
    on receiving !Google command. It tracks the search history by
    a algorithm. It breaks the !Google statement into words. For
    each word it calls makeKeyworks ehich breaks word into many
    possible subwords so that user can search over all subwords.
    """

    def track( self, message, sender_id ):
        store_service = StorageService()
        msg = store_service.addToMessages( message, sender_id )
        words = message.split(' ')

        for word in words:
            self.makeKeyworks( word, msg, sender_id )

    """
    Method compare sorts the response data based on rank followed by count
    """

    def compare( self, msg1, msg2 ):
        if msg1[1][0] < msg2[1][0]:
            return 1
        elif msg1[1][0] > msg2[1][0]:
            return -1
        else:
            if msg1[1][1] < msg2[1][1]:
                return 1
            else:
                return -1

    """
    Method getKeywordsForWords is called from coreSearch for fast query.
    If user types !Recent followed by N words, Here N db calls are done
    in parallel using 20 threads. This saves long waiting time in response.

    Here for each word out of N, a call is made to get all messages that contain
    that perticular word for that user id
    """

    def getKeywordsForWords( self, words, sender_id ):
        store_service = StorageService()
        executor = concurrent.futures.ThreadPoolExecutor( max_workers=20 )

        future_data = [executor.submit( store_service.getKeywordsByWord, word, sender_id) for word in words]

        keywords_data = []

        for future in concurrent.futures.as_completed( future_data ):
            keywords = future.result()
            data = []
            for keyword in keywords:
                data.append(keyword.message.message)
            keywords_data.append(data)

        return keywords_data

    """
    Method coreSearch is called by prepareResponse of AnsweringBot
    on receiving !Recent command
    This method calls getKeywordsForWords which uses threads to process
    the fast searching.
    for the command !Recent statement, here statement is broken into
    subwords and each word is searched in the database. For each word,
    it finds the search history and based on that it calculates which
    search history contain the most part of the statement and how much it
    was searched

    Example:
    !Recent This is awesome place to code
    Here each history is given a rank based on how much words it contains out
    of 'This','is','awesome','place','to','code' words. Then for all the history
    searches which have same rank, that search is chosen which came for maximum
    times in search history for that perticular user.
    """

    def coreSearch( self, words, sender_id ):
        store_service = StorageService()

        ranking = {}

        """
        outer_unique contains unique search history with how much words it
        contains out of words following !Recent command
        """
        outer_unique = {}

        if words[0] != '':
            keywords_data = self.getKeywordsForWords( words, sender_id )

            for keywords in keywords_data: # for each query word in !Recent command
                inner_unique = {}

                for keyword in keywords: #all the messages for that word
                    message = keyword

                    if message not in inner_unique:
                        inner_unique[message] = True
                        if message not in outer_unique:
                            outer_unique[message] = 1
                        else:
                            outer_unique[message] = outer_unique[message] + 1
            """
            Now store for how much time that perticular search history appears
            """
            for message in outer_unique:
                count = store_service.getMessageCount( message, sender_id )
                outer_unique[message] = (outer_unique[message],count)
        else:
            #if users types !Recent alone without any query words
            messages = store_service.getTopMessages( sender_id )

            inner_unique = {}

            for message in messages:
                message = message.message

                if message not in inner_unique:
                    inner_unique[message] = True
                    if message not in outer_unique:
                        outer_unique[message] = 1
                    else:
                        outer_unique[message] = outer_unique[message] + 1

            for message in outer_unique:
                count = store_service.getMessageCount( message, sender_id )
                outer_unique[message] = (outer_unique[message],count)

        result = list(outer_unique.items())

        # sory by rank followed by count
        result = sorted(result,key = cmp_to_key(self.compare))

        filtered_result = [ 'Results Sorted on Date, Rank and Number of times searched.' ]
        for res in result:
            res_msg = res[0] + ' - (keys match : ' + str(res[1][0]) + ',searched ' + str(res[1][1]) + ' times)'
            filtered_result.append(res_msg)

        filtered_result.append(' This does not include spell checking and any sensing ML algos ')

        return filtered_result[:20]
