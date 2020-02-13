from django.test import TestCase
from numista.services.coin_ex import CoinEx
from numista.tests.utils import Consts
from numista.models.country import Country
from numista.models.currency import Currency
from numista.tests.fixtures import FixtureCountries, FixtureCurrencies


class test_numista_coin(TestCase):
    databases = {'numista'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        FixtureCountries.init_Countries()
        FixtureCountries.COUNTRY_1.save()

    def test_coin_from_json_creates_country_and_currency(self):
        """
        Tests coin entity creation from json without mocking the currency and country entities.
        The country entity is pre-created in fixture, the currency needs to be created by the
        tested method along with the coin entity.
        """
        coin_ex = CoinEx.Coin_from_json(Consts.JSON.COIN_TEXT)
        self.assertEqual(
            coin_ex.numistaId, Consts.JSON.COIN_JSON['id'])
        self.assertEqual(
            coin_ex.url, Consts.JSON.COIN_JSON['url'])
        self.assertEqual(
            coin_ex.title, Consts.JSON.COIN_JSON['title'])
        self.assertEqual(
            coin_ex.country.code, Consts.JSON.COIN_JSON['country']['code'])
        self.assertEqual(
            coin_ex.country.name, Consts.JSON.COIN_JSON['country']['name'])
        self.assertEqual(
            coin_ex.minYear, Consts.JSON.COIN_JSON['minYear'])
        self.assertEqual(
            coin_ex.maxYear, Consts.JSON.COIN_JSON['maxYear'])
        self.assertEqual(
            coin_ex.coinType, Consts.JSON.COIN_JSON['type'])
        self.assertEqual(
            coin_ex.valueText, Consts.JSON.COIN_JSON['value']['text'])
        self.assertEqual(
            coin_ex.valueCurrency.numistaId, Consts.JSON.COIN_JSON['value']['currency']['id'])
        self.assertEqual(
            coin_ex.valueCurrency.name, Consts.JSON.COIN_JSON['value']['currency']['name'])
        self.assertEqual(
            coin_ex.shape, Consts.JSON.COIN_JSON['shape'])
        self.assertEqual(
            coin_ex.composition, Consts.JSON.COIN_JSON['composition']['text'])
        self.assertEqual(
            coin_ex.weight, Consts.JSON.COIN_JSON['weight'])
        self.assertEqual(
            coin_ex.size, Consts.JSON.COIN_JSON['size'])
        if 'thickness' in Consts.JSON.COIN_JSON:
            self.assertEqual(
                coin_ex.thickness, Consts.JSON.COIN_JSON['thickness'])
        self.assertEqual(
            coin_ex.obverse_picture, Consts.JSON.COIN_JSON['obverse']['picture'])
        self.assertEqual(
            coin_ex.obverse_thumbnail, Consts.JSON.COIN_JSON['obverse']['thumbnail'])
        self.assertEqual(
            coin_ex.reverse_picture, Consts.JSON.COIN_JSON['reverse']['picture'])
        self.assertEqual(
            coin_ex.reverse_thumbnail, Consts.JSON.COIN_JSON['reverse']['thumbnail'])

        country = Country.objects.get(code=coin_ex.country.code)
        self.assertEqual(country.name, coin_ex.country.name)

        currency = Currency.objects.get(
            numistaId=coin_ex.valueCurrency.numistaId)
        self.assertEqual(currency.name, coin_ex.valueCurrency.name)
