from discordsearch.services.StorageService import StorageService

class CoreService:

    def makeKeyworks( self, word, msg ):
        length = len(word)
        N = length

        while N > 0:
            for i in range(0,length-N+1):
                subword = word[i:i+N]
                store_service = StorageService()
                store_service.addToKeywords( msg, subword )

            N = N-1

    def track( self, message, sender_id ):
        store_service = StorageService()
        msg = store_service.addToMessages( message, sender_id )
        words = message.split(' ')

        for word in words:
            self.makeKeyworks( word, msg )

    def coreSearch( self, words ):
        store_service = StorageService()

        for word in words:
            keywords = store_service.getMessagesByKeyword( word )

            for keyword in keywords:
                print(keyword.message.message)
                print(keyword.message.created_time)

        #keywords
        return ['finding']
