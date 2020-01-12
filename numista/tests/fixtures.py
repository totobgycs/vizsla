from .utils import Consts, RunOnce 

from numista.models import Country
class FixtureCountries:

    @classmethod
    @RunOnce
    def init_Countries(cls):
       cls.COUNTRY_1 = Country(
            code = Consts.COUNTRY.CODE_1,
            name = Consts.COUNTRY.NAME_1
       )
       cls.COUNTRY_1.save()

from numista.models import Currency
class FixtureCurrencies:

    @classmethod
    @RunOnce
    def init_Currencies(cls):
       cls.CURRENCY_1 = Currency(
            numistaId = Consts.CURRENCY.NUMISTA_ID_1,
            name = Consts.CURRENCY.NAME_1
       )
       cls.CURRENCY_1.save()

from numista.models import Coin
class FixtureCoins:

    @classmethod
    @RunOnce
    def init_Coins(cls):
       FixtureCountries.init_Countries()
       FixtureCurrencies.init_Currencies()
       cls.COIN_1 = Coin(
            numistaId = Consts.COIN.NUMISTA_ID_1,
            title = Consts.COIN.NAME_1,
            country = FixtureCountries.COUNTRY_1,
            valueCurrency = FixtureCurrencies.CURRENCY_1
       )
       cls.COIN_1.save()
