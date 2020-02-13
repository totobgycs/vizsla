import requests
from vizsla import settings


class NumistaClient:

    NUMISTA_URL = 'https://api.numista.com/api/v1/'
    NUMISTA_SEARCH_COIN = 'coins'
    NUMISTA_GET_COIN = 'coins/%s'
    NUMISTA_GET_ISSUES = 'coins/%s/issues'

    ERRORS = {
        400	: 'Invalid parameter or missing mandatory parameter',
        401	: 'Invalid or missing API key',
        404	: 'The coin with given ID was not found',
        429	: 'Quota exceeded',
    }

    def __init__(self, api_key=None):
        if api_key == None:
            api_key = settings.NUMISTA_KEY
        self.api_key = api_key
        self.HEADER = {'Numista-API-Key': api_key}

    def __execute_function(self, function, params):
        r = requests.get(
            self.NUMISTA_URL + function, headers=self.HEADER, params=params)
        if r.status_code in self.ERRORS:
            raise Exception(self.ERRORS[r.status_code])
        return r.json()

    def search_coins(self, query, language='en', pages=1, per_page=50):
        """
        Search for coins. 
        Parameters
        ----------
            query (str): Coin names to search for
            languge (str): Language for saerch and response (accepted 'en' and 'fr', default 'en')
            pages (int): number of pages to return (default 1)
            per_page (int): results per page (default 50)
        """
        payload = {'lang': language, 'q': query,
                   'page': pages, 'count': per_page}
        return self.__execute_function(self.NUMISTA_SEARCH_COIN, payload)

    def get_coin(self, coin, language='en'):
        """
        Get informations of a specific coin. 
        Parameters
        ----------
            coin (str): Numista id of the coin (got from search_coins)
            languge (str): Language for saerch and response (accepted 'en' and 'fr', default 'en')
        """
        payload = {'lang': language}
        return self.__execute_function(self.NUMISTA_GET_COIN % coin, payload)

    def get_coin_issues(self, coin, language='en'):
        """
        Get issue informations of a specific coin. 
        Parameters
        ----------
            coin (str): Numista id of the coin (got from search_coins)
            languge (str): Language for saerch and response (accepted 'en' and 'fr', default 'en')
        """
        payload = {'lang': language}
        return self.__execute_function(self.NUMISTA_GET_ISSUES % coin, payload)
