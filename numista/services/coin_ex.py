from numista.models.coin import Coin
from numista.models.country import Country
from numista.models.currency import Currency
from .numista import NumistaClient
import json
from flatten_json import flatten


class CoinEx(Coin):

    class Meta:
        proxy = True

    @classmethod
    def Coin_from_json(cls, coin_json):
        obj = json.loads(coin_json)
        result = cls(
            numistaId=obj['id'],
            title=obj['title']
        )

        if 'country' in obj:
            cntry, _ = Country.objects.get_or_create(
                code=obj['country']['code'], defaults=obj['country'])
            result.country = cntry
        if 'value' in obj and 'currency' in obj['value']:
            curr, _ = Currency.objects.get_or_create(
                numistaId=obj['value']['currency']['id'], defaults=obj['value']['currency'])
            result.value_currency = curr

        flat_obj = flatten(obj)
        for f in Coin._meta.get_fields():
            if f.name == 'id':
                pass
            elif (f.name in flat_obj) and (getattr(result, f.name) in f.empty_values):
                setattr(result, f.name, flat_obj[f.name])
            elif hasattr(f, 'json_id') and (f.json_id in flat_obj) and (getattr(result, f.name) in f.empty_values):
                setattr(result, f.name, flat_obj[f.json_id])
        return result

    @classmethod
    def Coin_from_numista_id(cls, numista_id):
        numistaClient = NumistaClient()
        return cls.Coin_from_json(numistaClient.get_coin(numista_id))
