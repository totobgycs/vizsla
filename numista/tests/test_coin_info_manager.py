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
        Test coin and isues info getting based on numista id
        """
        coin_info_json = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        mock_numista_client.return_value.get_coin.return_value = coin_info_json

        coin_issues_json = Consts.JSON_ISSUE.ONE_ISSUE_JSON
        mock_numista_client.return_value.get_coin_issues.return_value = coin_issues_json

        coin_res, issue_res = self.coin_info_manager.get_from_numista_id(
            coin_info_json['id'])

        self.assertDictEqual(coin_res, coin_info_json)
        self.assertDictEqual(issue_res[0], coin_issues_json[0])

    @patch.object(CoinInfoManager, 'get_from_numista_id')
    def test_get_or_retrive_non_existent(self, mock_get_from_numista_id):
        """
        Test coin and isues info getting or retrieveing based on numista id
        In this case the date does not esist in the cache database, so it is 
        get from numista
        """

        coin_info_json = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        coin_issues_json = Consts.JSON_ISSUE.ONE_ISSUE_JSON

        mock_get_from_numista_id.return_value = (coin_info_json, coin_issues_json)

        coin_res, issue_res = self.coin_info_manager.get_or_retrive(coin_info_json['id'])

        self.assertDictEqual(coin_res, coin_info_json)
        self.assertDictEqual(issue_res[0], coin_issues_json[0])
        mock_get_from_numista_id.assert_called_once()

    @patch.object(CoinInfoManager, 'get_from_numista_id')
    def test_get_or_retrive_existent(self, mock_get_from_numista_id):
        """
        Test coin and isues info getting or retrieveing based on numista id
        In the first call the data is got from numista
        In the second call the data already esist in the cache database, so it is 
        returned, without going to numista.
        """

        coin_info_json = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        coin_issues_json = Consts.JSON_ISSUE.ONE_ISSUE_JSON

        mock_get_from_numista_id.return_value = (coin_info_json, coin_issues_json)

        self.coin_info_manager.get_or_retrive(coin_info_json['id'])
        mock_get_from_numista_id.assert_called_once()

        coin_res, issue_res = self.coin_info_manager.get_or_retrive(coin_info_json['id'])

        self.assertDictEqual(coin_res, coin_info_json)
        self.assertDictEqual(issue_res[0], coin_issues_json[0])
        mock_get_from_numista_id.assert_called_once()

    @patch('numista.models.coin_info_manager.settings')
    @patch.object(CoinInfoManager, 'get_from_numista_id')
    def test_get_or_retrive_existent_refresh(self, mock_get_from_numista_id, mock_settings):
        """
        Test coin and isues info getting or retrieveing based on numista id
        In the first call the data is got from numista
        In the second call the data already esist in the cache database, but the refresh period
        is set to -1 so it is got again from numista.
        """

        coin_info_json = Consts.JSON_COIN.COIN_JSON_MINIMAL_1
        coin_issues_json = Consts.JSON_ISSUE.ONE_ISSUE_JSON

        mock_get_from_numista_id.return_value = (coin_info_json, coin_issues_json)
        mock_settings.NUMISTA_REFRESH_DAYS = -1

        self.coin_info_manager.get_or_retrive(coin_info_json['id'])
        mock_get_from_numista_id.assert_called_once()

        coin_res, issue_res = self.coin_info_manager.get_or_retrive(coin_info_json['id'])

        self.assertDictEqual(coin_res, coin_info_json)
        self.assertDictEqual(issue_res[0], coin_issues_json[0])
        self.assertEqual(2, mock_get_from_numista_id.call_count)
