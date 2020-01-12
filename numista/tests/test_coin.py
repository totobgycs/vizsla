from django.test import TestCase
from numista.models import Coin
from numista.tests.utils import Consts
from numista.tests.fixtures import FixtureCountries, FixtureCurrencies
import django.db.utils

class test_numista_model(TestCase):
    databases = {'numista'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        FixtureCountries.init_Countries()
        FixtureCurrencies.init_Currencies()

      
    def test_add(self):
        coin=Coin(
            numistaId = Consts.COIN.NUMISTA_ID_1,
            title = Consts.COIN.NAME_1,
            country = FixtureCountries.COUNTRY_1,
            valueCurrency = FixtureCurrencies.CURRENCY_1
        )
        coin.save()

        result=Coin.objects.get(numistaId = Consts.COIN.NUMISTA_ID_1)

        # self.assertEqual(result.count, 1)
        self.assertEqual(result.title, Consts.COIN.NAME_1)
        self.assertEqual(str(result), '{}: {}'.format(Consts.COIN.NUMISTA_ID_1, Consts.COIN.NAME_1))

    def test_add_duplicate_fails(self):
        coin=Coin(
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            title = Consts.COIN.NAME_1,
            country = FixtureCountries.COUNTRY_1,
            valueCurrency = FixtureCurrencies.CURRENCY_1
        )
        coin.save()

        coin=Coin(
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            title = Consts.COIN.NAME_2,
            country = FixtureCountries.COUNTRY_1,
            valueCurrency = FixtureCurrencies.CURRENCY_1
        )

        with self.assertRaises(django.db.utils.IntegrityError):
            coin.save()

    def test_add_duplicate_coin(self):
        coin=Coin(
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            title = Consts.COIN.NAME_1,
            country = FixtureCountries.COUNTRY_1,
            valueCurrency = FixtureCurrencies.CURRENCY_1
        )
        coin.save()

        coin=Coin(
            numistaId = Consts.ISSUE.NUMISTA_ID_2,
            title = Consts.COIN.NAME_1,
            country = FixtureCountries.COUNTRY_1,
            valueCurrency = FixtureCurrencies.CURRENCY_1
        )
        coin.save()

        result = Coin.objects.filter(title = Consts.COIN.NAME_1).all()

        self.assertEqual(result.count(), 2)        
