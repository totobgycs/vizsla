from django.test import TestCase
from numista.models import Issue
from .utils import Consts
from .fixtures import FixtureCoins
import django.db.utils

class test_numista_model(TestCase):
    databases = {'numista'}

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        FixtureCoins.init_Coins()

      
    def test_add(self):
        issue=Issue(
            coin = FixtureCoins.COIN_1,
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            isDated = True,
            year = Consts.ISSUE.YEAR_1
        )
        issue.save()

        result=Issue.objects.get(numistaId = Consts.ISSUE.NUMISTA_ID_1)

        # self.assertEqual(result.count, 1)
        self.assertEqual(result.year, Consts.ISSUE.YEAR_1)
        self.assertEqual(str(result), '{}: {} {}'.format(Consts.ISSUE.NUMISTA_ID_1, Consts.COIN.NAME_1, Consts.ISSUE.YEAR_1))

    def test_add_duplicate_fails(self):
        issue=Issue(
            coin = FixtureCoins.COIN_1,
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            isDated = True,
            year = Consts.ISSUE.YEAR_1
        )
        issue.save()

        issue=Issue(
            coin = FixtureCoins.COIN_1,
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            isDated = True,
            year = Consts.ISSUE.YEAR_2
        )

        with self.assertRaises(django.db.utils.IntegrityError):
            issue.save()

    def test_add_duplicate_year(self):
        issue=Issue(
            coin = FixtureCoins.COIN_1,
            numistaId = Consts.ISSUE.NUMISTA_ID_1,
            isDated = True,
            year = Consts.ISSUE.YEAR_1
        )
        issue.save()

        issue=Issue(
            coin = FixtureCoins.COIN_1,
            numistaId = Consts.ISSUE.NUMISTA_ID_2,
            isDated = True,
            year = Consts.ISSUE.YEAR_1
        )
        issue.save()

        result = Issue.objects.filter(year = Consts.ISSUE.YEAR_1).all()

        self.assertEqual(result.count(), 2)        
