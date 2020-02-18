from django.test import TestCase
from unittest.mock import patch, Mock

from numista.models.coin_manager import CoinManager
from numista.tests.utils import Consts
from numista.models.coin import Coin
from numista.models.country import Country
from numista.models.currency import Currency
from numista.tests.fixtures import FixtureCountries, FixtureCurrencies


class test_numista_coin(TestCase):
    databases = {'numista'}

    coin_manager = CoinManager()
    coin_manager.model=Coin

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        FixtureCountries.init_Countries()
        FixtureCountries.COUNTRY_1.save()

    def __assert_common(self, coin_ex, json):
        self.assertEqual(
            coin_ex.numistaId, json['id'])
        self.assertEqual(
            coin_ex.url, json['url'])
        self.assertEqual(
            coin_ex.title, json['title'])
        self.assertEqual(
            coin_ex.minYear, json['minYear'])
        self.assertEqual(
            coin_ex.maxYear, json['maxYear'])
        self.assertEqual(
            coin_ex.coinType, json['type'])
        self.assertEqual(
            coin_ex.shape, json['shape'])
        self.assertEqual(
            coin_ex.composition_text, json['composition']['text'])
        self.assertEqual(
            coin_ex.weight, json['weight'])
        self.assertEqual(
            coin_ex.size, json['size'])
        self.assertEqual(
            coin_ex.obverse_picture, json['obverse']['picture'])
        self.assertEqual(
            coin_ex.obverse_thumbnail, json['obverse']['thumbnail'])
        self.assertEqual(
            coin_ex.reverse_picture, json['reverse']['picture'])
        self.assertEqual(
            coin_ex.reverse_thumbnail, json['reverse']['thumbnail'])


    def test_coin_from_json_creates_country_and_currency(self):
        """
        Tests coin entity creation from json without mocking the currency and country entities.
        The country entity is pre-created in fixture, the currency needs to be created by the
        tested method along with the coin entity.
        """
        json = Consts.JSON.COIN_JSON
        coin_ex=self.coin_manager.get_from_json(json)

        self.__assert_common(coin_ex, json)

        self.assertEqual(
            coin_ex.country.code, json['country']['code'])
        self.assertEqual(
            coin_ex.country.name, json['country']['name'])
        self.assertEqual(
            coin_ex.value_text, json['value']['text'])
        self.assertEqual(
            coin_ex.value_currency.numistaId, json['value']['currency']['id'])
        self.assertEqual(
            coin_ex.value_currency.name, json['value']['currency']['name'])

        country = Country.objects.get(code=coin_ex.country.code)
        self.assertEqual(country.name, coin_ex.country.name)

        currency = Currency.objects.get(
            numistaId=coin_ex.value_currency.numistaId)
        self.assertEqual(currency.name, coin_ex.value_currency.name)

    def test_coin_from_json_no_country(self):
        """
        Tests coin entity creation from json without mocking the currency and country entities.
        The country entity is pre-created in fixture, the currency needs to be created by the
        tested method along with the coin entity.
        """
        json = Consts.JSON.COIN_JSON_NO_COUNTRY
        coin_ex=self.coin_manager.get_from_json(json)

        self.__assert_common(coin_ex, json)

        self.assertEqual(
            coin_ex.value_text, json['value']['text'])
        self.assertEqual(
            coin_ex.value_currency.numistaId, json['value']['currency']['id'])
        self.assertEqual(
            coin_ex.value_currency.name, json['value']['currency']['name'])

    def test_coin_from_json_value_no_currency(self):
        """
        Tests coin entity creation from json without mocking the currency and country entities.
        The country entity is pre-created in fixture, the currency needs to be created by the
        tested method along with the coin entity.
        """
        json = Consts.JSON.COIN_JSON_VALUE_NO_CURRENCY
        coin_ex=self.coin_manager.get_from_json(json)

        self.__assert_common(coin_ex, json)

        self.assertEqual(
            coin_ex.country.code, json['country']['code'])
        self.assertEqual(
            coin_ex.country.name, json['country']['name'])
        self.assertEqual(
            coin_ex.value_text, json['value']['text'])

    def test_coin_from_json_no_value(self):
        """
        Tests coin entity creation from json without mocking the currency and country entities.
        The country entity is pre-created in fixture, the currency needs to be created by the
        tested method along with the coin entity.
        """
        json = Consts.JSON.COIN_JSON_NO_VALUE
        coin_ex=self.coin_manager.get_from_json(json)

        self.__assert_common(coin_ex, json)

        self.assertEqual(
            coin_ex.country.code, json['country']['code'])
        self.assertEqual(
            coin_ex.country.name, json['country']['name'])
        self.assertEqual(
            coin_ex.thickness, json['thickness'])

    @patch('numista.services.numista.NumistaClient')
    def test_coin_from_numista_id(self, mock_numista_client):
        mock_numista_client.get_coin.return_value=Consts.JSON.COIN_TEXT
        coin_ex=self.coin_manager.get_from_numista_id(Consts.JSON.COIN_JSON['id'])


    def test_integrated_coin_from_json(self):
        """
        Test coin entity cration together with the Coin model
        """

        json = Consts.JSON.COIN_JSON
        coin_ex=self.coin_manager.get_from_json(json)

        self.__assert_common(coin_ex, json)

