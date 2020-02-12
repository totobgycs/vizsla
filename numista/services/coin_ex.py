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
        cntry, _ = Country.objects.get_or_create(code=obj['country']['code'], defaults=obj['country'])
        curr , _ = Currency.objects.get_or_create(numistaId=obj['value']['currency']['id'], defaults=obj['value']['currency'])
        result = cls(
            numistaId=obj['id'],
            title=obj['title']
        )
        
        for f in Coin._meta.get_fields(include_hidden=True):
            pass

        #     url=obj['url'],
        #     country=cntry,
        #     minYear=obj['minYear'],
        #     maxYear=obj['maxYear'],
        #     coinType=obj['type'],
        #     valueText=obj['value']['text'],
        #     valueCurrency=curr,
        #     shape=obj['shape'],
        #     composition=obj['composition']['text'],
        #     weight=obj['weight'],
        #     size=obj['size'],
        #     thickness=obj.get('thickness', None),
        #     obverse_picture=obj['obverse']['picture'],
        #     obverse_thumbnail=obj['obverse']['thumbnail'],
        #     reverse_picture=obj['reverse']['picture'],
        #     reverse_thumbnail=obj['reverse']['thumbnail']
        # )

    @classmethod
    def Coin_from_numista_id(cls, numista_id):
        numistaClient = NumistaClient()
        return cls.Coin_from_json(numistaClient.get_coin(numista_id))
