from discordsearch.services.StorageService import StorageService
from functools import cmp_to_key
import random
import concurrent.futures

class CoreService:

    def makeKeyworks( self, word, msg, sender_id ):
        length = len(word)
        N = length

        while N > 0:
            for i in range(0,length-N+1):
                subword = word[i:i+N]
                store_service = StorageService()
                store_service.addToKeywords( msg, subword, sender_id )

            N = N-1

    def track( self, message, sender_id ):
        store_service = StorageService()
        msg = store_service.addToMessages( message, sender_id )
        words = message.split(' ')

        for word in words:
            self.makeKeyworks( word, msg, sender_id )

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

    def getKeywordsForWords( self, words, sender_id ):
        store_service = StorageService()
        executor = concurrent.futures.ThreadPoolExecutor( max_workers=40 )

        future_data = [executor.submit( store_service.getMessagesByKeyword, word, sender_id) for word in words]

        keywords_data = []

        for future in concurrent.futures.as_completed( future_data ):
            keywords = future.result()
            data = []
            for keyword in keywords:
                data.append(keyword.message.message)
            keywords_data.append(data)

        return keywords_data

    def coreSearch( self, words, sender_id ):
        store_service = StorageService()

        ranking = {}
        sorted_result = []
        outer_unique = {}

        keywords_data = self.getKeywordsForWords( words, sender_id )

        for keywords in keywords_data:
            inner_unique = {}

            for keyword in keywords:
                message = keyword

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
        result = sorted(result,key = cmp_to_key(self.compare))

        filtered_result = [ 'Results Sorted on Date, Rank and Number of times searched.' ]
        for res in result:
            res_msg = res[0] + ' - (keys match : ' + str(res[1][0]) + ',searched ' + str(res[1][1]) + ' times)'
            filtered_result.append(res_msg)

        filtered_result.append(' This does not include spell checking and any sensing ML algos ')

        return filtered_result
