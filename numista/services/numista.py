from enum import Enum
import requests


class NumistaClient:

    NUMISTA_URL = 'https://api.numista.com/api/v1/coins'

    ERRORS = {
        400	: 'Invalid parameter or missing mandatory parameter',
        401	: 'Invalid or missing API key',
        404	: 'The coin with given ID was not found',
        429	: 'Quota exceeded',
    }

    def __init__(self, api_key):
        self.api_key = api_key
        self.HEADER = {'Numista-API-Key': api_key}

    def search_coins(self, query, language='en', pages=1, per_page=50):
        payload = {'lang': language, 'q': query,
                   'page': pages, 'count': per_page}
        r = requests.get(self.NUMISTA_URL, headers=self.HEADER, params=payload)
        if r.status_code in self.ERRORS:
            raise Exception(self.ERRORS[r.status_code])
        return r.json()

    def get_coin(self, coin, language='en'):
        payload = {'lang': language}
        r = requests.get(self.NUMISTA_URL + '/' + str(coin), headers=self.HEADER, params=payload)
        if r.status_code in self.ERRORS:
            raise Exception(self.ERRORS[r.status_code])
        return r.json()

    def get_coin_issues(self, coin, language='en'):
        payload = {'lang': language}
        r = requests.get(self.NUMISTA_URL + '/' + str(coin) + '/issues', headers=self.HEADER, params=payload)
        if r.status_code in self.ERRORS:
            raise Exception(self.ERRORS[r.status_code])
        return r.json()
