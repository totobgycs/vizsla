from django.test import TestCase
from numista.models import CoinInfo
from numista.tests.utils import Consts
import django.db.utils

class test_numista_coin_info(TestCase):
    databases = {'numista'}

    # just for reference
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_add(self):
        coin = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        coin_info = CoinInfo(
            numistaId=coin['id'],
            numistaCoin=coin
        )
        coin_info.save()

        result = CoinInfo.objects.get(numistaId=coin['id'])

        self.assertEqual(result.numistaCoin, coin)
        self.assertEqual(str(result), '{}: {}'.format(
            coin['id'], coin['title']))

    def test_add_duplicate_fails(self):
        coin = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        coin_info = CoinInfo(
            numistaId=coin['id'],
            numistaCoin=coin
        )
        coin_info.save()

        coin_info = CoinInfo(
            numistaId=coin['id'],
            numistaCoin=coin
        )

        with self.assertRaises(django.db.utils.IntegrityError):
            coin_info.save()

    def test_add_duplicate_title(self):
        coin = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        coin_info = CoinInfo(
            numistaId=coin['id'],
            numistaCoin=coin
        )
        coin_info.save()

        coin = Consts.JSON_COIN.COIN_JSON_MINIMAL_2
        coin_info = CoinInfo(
            numistaId=coin['id'],
            numistaCoin=coin
        )
        coin_info.save()

        result = CoinInfo.objects.filter(numistaCoin__title=coin['title']).all()

        self.assertEqual(result.count(), 2)

