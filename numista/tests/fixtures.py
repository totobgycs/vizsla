from numista.models import Coin
from numista.models import Currency
from .utils import Consts, RunOnce

from numista.models import Country


class FixtureCountries:

    @classmethod
    @RunOnce
    def init_Countries(cls):
        cls.COUNTRY_1 = Country(
            code=Consts.COUNTRY.CODE_1,
            name=Consts.COUNTRY.NAME_1
        )


class FixtureCurrencies:

    @classmethod
    @RunOnce
    def init_Currencies(cls):
        cls.CURRENCY_1 = Currency(
            numistaId=Consts.CURRENCY.NUMISTA_ID_1,
            name=Consts.CURRENCY.NAME_1
        )


class FixtureCoins:

    @classmethod
    @RunOnce
    def init_Coins(cls):
        FixtureCountries.init_Countries()
        cls.COUNTRY_1 = FixtureCountries.COUNTRY_1
        FixtureCurrencies.init_Currencies()
        cls.CURRENCY_1 = FixtureCurrencies.CURRENCY_1
        cls.COIN_1 = Coin(
            numistaId=Consts.COIN.NUMISTA_ID_1,
            title=Consts.COIN.NAME_1,
            country=cls.COUNTRY_1,
            value_currency=cls.CURRENCY_1
        )
