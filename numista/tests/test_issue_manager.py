from django.test import TestCase
from unittest.mock import patch, Mock

from numista.models.Issue_manager import IssueManager
from numista.tests.utils import Consts
from numista.models.issue import Issue
from numista.tests.fixtures import FixtureCoins, FixtureCountries, FixtureCurrencies


class test_numista_issue_manager(TestCase):
    databases = {'numista'}

    issue_manager = IssueManager()
    issue_manager.model = Issue

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        FixtureCoins.init_Coins()
        FixtureCountries.COUNTRY_1.save()
        FixtureCurrencies.CURRENCY_1.save()
        FixtureCoins.COIN_1.save()

    def __assert_common(self, coin_ex, json):
        self.assertEqual(
            coin_ex.numistaId, json['id'])

    def test_one_issue_is_created(self):
        json=Consts.JSON_ISSUE.ONE_ISSUE_JSON
        issues=self.issue_manager.get_from_json(Consts.COIN.NUMISTA_ID_1, json)
        for issue in issues:
            self.__assert_common(issue, json[0])

