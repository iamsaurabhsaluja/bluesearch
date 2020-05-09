try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

class SearchGoogle:

    """
    Method topResults is called by AnsweringBot on
    receiving !Google command from user
    topResults gets the top N google results.
    This uses googlesearch python library
    """

    def topResults( self, query, limit ):

        search_results = []
        for res in search(query, tld="co.in", num=limit, stop=limit, pause=0):
            search_results.append( res )

        return search_results
