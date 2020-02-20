from django.db import models

from numista.models.country import Country
from numista.models.currency import Currency
from numista.services.numista import NumistaClient

import json
from flatten_json import flatten


class CoinManager(models.Manager):
    def get_from_json(self, coin_json: dict):
        """
        Creates a Coin model entit from a json (dict).
        Parameters
        ----------
            coin_json (json): json descrioption of coin as returned by Numista
        """
        result = self.model(
            numistaId=coin_json['id'],
            title=coin_json['title']
        )
        if 'country' in coin_json:
            cntry, _ = Country.objects.get_or_create(
                code=coin_json['country']['code'], defaults=coin_json['country'])
            result.country = cntry
        if 'value' in coin_json and 'currency' in coin_json['value']:
            curr, _ = Currency.objects.get_or_create(
                numistaId=coin_json['value']['currency']['id'], defaults=coin_json['value']['currency'])
            result.value_currency = curr

        flat_obj = flatten(coin_json)
        for f in self.model._meta.get_fields():
            if f.name == 'id':
                pass
            elif (f.name in flat_obj) and (getattr(result, f.name) in f.empty_values):
                setattr(result, f.name, flat_obj[f.name])
            elif hasattr(f, 'json_id') and (f.json_id in flat_obj) and (getattr(result, f.name) in f.empty_values):
                setattr(result, f.name, flat_obj[f.json_id])
        return result

    def get_from_numista_id(self, numista_id):
        """
        Create a Coin model entity based on the NumistaId, by getting information from numista.com
        Parameters
        ----------
            numista_id : numista id of coin to be created. 
        """
        numistaClient = NumistaClient()
        return self.get_from_json(numistaClient.get_coin(numista_id))
