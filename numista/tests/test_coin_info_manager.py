from django.test import TestCase
from unittest.mock import patch, Mock

from numista.models.coin_info_manager import CoinInfoManager
from numista.models.coin_info import CoinInfo
from numista.tests.utils import Consts

class test_numista_coin_info_mnager(TestCase):
    databases = {'numista'}

    coin_info_manager = CoinInfoManager()
    coin_info_manager.model = CoinInfo

    @patch('numista.models.coin_info_manager.NumistaClient')
    def test_get_from_numista_id(self, mock_numista_client):
        """
        Test coin nad isuues info getting based on numista id
        """
        coin_info_json = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        mock_numista_client.return_value.get_coin.return_value = coin_info_json

        coin_issues_json = Consts.JSON_ISSUE.ONE_ISSUE_JSON 
        mock_numista_client.return_value.get_coin_issues.return_value = coin_issues_json

        coin_res, issue_res = self.coin_info_manager.get_from_numista_id(coin_info_json['id'])

        self.assertDictEqual(coin_res, coin_info_json)
        self.assertDictEqual(issue_res[0], coin_issues_json[0])

    # @patch('coin_info_manager.get_from_numista_id')
    # def test_