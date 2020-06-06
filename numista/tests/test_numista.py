from django.test import SimpleTestCase
from unittest.mock import patch, Mock

from numista.services.numista import NumistaClient
from .utils import Consts


class test_numista_interface(SimpleTestCase):

    API_KEY = 'api_key'
    RESPONSE_JSON = 'json'
    COIN_PARAM = 'par1'
    LANG_PARAM = 'xx'
    PAGE_PARAM = 3
    COUNT_PARAM = 20

    @classmethod
    def setUpClass(cls):
        """ Create a NumistaClient to test """
        super().setUpClass()
        cls.numistaClient = NumistaClient(cls.API_KEY)

    # region Utils
    def __ok_mock(self):
        """ Create a mock of Requests get, which returns success and a response """
        retval_mock = Mock()
        retval_mock.status_code = 200
        retval_mock.json.return_value = self.RESPONSE_JSON
        return retval_mock

    def __error_mock(self, code):
        """ 
        Create a mock of Requests get, which returns an error
        Parameters
        ----------
            code (int): The error code to return
        """
        retval_mock = Mock()
        retval_mock.status_code = code
        return retval_mock

    # endregion

    # region Generic Test Methods
    def __raises_exception_on_error(self, mock_request, method_to_test, *args):
        """
        Tests if method_to_test raises an exception when requests.get returns an error code
        Parameters
        ----------
            mock_request (Mock()): mock of requests.get
            method_to_test (method): The method to test
            *args: Parameters transmitted to method_to_test
        """
        for error in NumistaClient.ERRORS:
            mock_request.get.return_value = self.__error_mock(error)
            self.assertRaisesMessage(
                Exception, NumistaClient.ERRORS[error], method_to_test, *args)

    def __returns_json(self, mock_request, method_to_test, *args):
        """
        Tests if method_to_test returns the json part of the response given by requestes.get 
        Parameters
        ----------
            mock_request (Mock): mock of requests.get
            method_to_test (method): The method to test
            *args: Parameters transmitted to method_to_test
        """
        mock_request.get.return_value = self.__ok_mock()
        result = method_to_test(*args)
        self.assertEqual(result, self.RESPONSE_JSON)

    def __get_is_called_with_params(self, mock_request, method_to_test, param='', expected_function='', expected_params={}, **kwargs):
        """
        Tests if method_to_test called with param and **kwargs will call requestes.get with the expected parameters
        Parameters
        ----------
            mock_request (Mock): mock of requests.get
            method_to_test (method): The method to test
            param: The parameter of method_to_test
            expected_function (str): The expected endpoint function with which requests.get is called
            expected_param (kwargs): The expected extra params with which requests.get is called
            **kwargs: Parameters transmitted to method_to_test
        """
        mock_request.get.return_value = self.__ok_mock()
        method_to_test(param, **kwargs)
        mock_args, mock_kwargs = mock_request.get.call_args.args, mock_request.get.call_args.kwargs
        self.assertEqual(mock_args, expected_function)
        self.assertEqual(mock_kwargs['headers'], self.numistaClient.HEADER)
        self.assertEqual(mock_kwargs['params'], expected_params)

    # endregion

    # region get_coin
    @patch('numista.services.numista.requests')
    def test_get_coin_returns_json(self, mock_request):
        self.__returns_json(
            mock_request, self.numistaClient.get_coin, self.COIN_PARAM)

    @patch('numista.services.numista.requests')
    def test_get_coin_is_called_with_params(self, mock_request):
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.get_coin,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_GET_COIN % self.COIN_PARAM,),
            expected_params={'lang': 'en'})
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.get_coin,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_GET_COIN % self.COIN_PARAM,),
            expected_params={'lang': self.LANG_PARAM},
            language=self.LANG_PARAM)

    @patch('numista.services.numista.requests')
    def test_get_coin_raises_exception_on_error(self, mock_request):
        self.__raises_exception_on_error(
            mock_request, self.numistaClient.get_coin, self.COIN_PARAM)

    # endregion

    # region search_coin
    @patch('numista.services.numista.requests')
    def test_search_coin_issues_returns_json(self, mock_request):
        self.__returns_json(
            mock_request, self.numistaClient.search_coins, self.COIN_PARAM)

    @patch('numista.services.numista.requests')
    def test_search_coin_is_called_with_params(self, mock_request):
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.search_coins,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_SEARCH_COIN,),
            expected_params={
                'lang': 'en',
                'q': self.COIN_PARAM,
                'page': 1,
                'count': 50})
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.search_coins,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_SEARCH_COIN,),
            expected_params={
                'lang': self.LANG_PARAM,
                'q': self.COIN_PARAM,
                'page': 1,
                'count': 50},
            language=self.LANG_PARAM)
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.search_coins,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_SEARCH_COIN,),
            expected_params={
                'lang': 'en',
                'q': self.COIN_PARAM,
                'page': self.PAGE_PARAM,
                'count': 50},
            pages=self.PAGE_PARAM)
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.search_coins,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_SEARCH_COIN,),
            expected_params={
                'lang': 'en',
                'q': self.COIN_PARAM,
                'page': 1,
                'count': self.COUNT_PARAM},
            per_page=self.COUNT_PARAM)

    @patch('numista.services.numista.requests')
    def test_get_coin_issues_raises_exception_on_error(self, mock_request):
        self.__raises_exception_on_error(
            mock_request, self.numistaClient.get_coin_issues, self.COIN_PARAM)

    # endregion

    # region get_coin_issues
    @patch('numista.services.numista.requests')
    def test_get_coin_issues_returns_json(self, mock_request):
        self.__returns_json(
            mock_request, self.numistaClient.get_coin_issues, self.COIN_PARAM)

    @patch('numista.services.numista.requests')
    def test_get_coin_issues_is_called_with_params(self, mock_request):
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.get_coin_issues,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_GET_ISSUES % self.COIN_PARAM,),
            expected_params={'lang': 'en'})
        self.__get_is_called_with_params(
            mock_request, self.numistaClient.get_coin,
            param=self.COIN_PARAM,
            expected_function=(
                self.numistaClient.NUMISTA_URL + self.numistaClient.NUMISTA_GET_COIN % self.COIN_PARAM,),
            expected_params={'lang': self.LANG_PARAM},
            language=self.LANG_PARAM)

    @patch('numista.services.numista.requests')
    def test_search_coins_raises_exception_on_error(self, mock_request):
        self.__raises_exception_on_error(
            mock_request, self.numistaClient.search_coins, self.COIN_PARAM)

    # endregion
    # region UnMocked
    # def test_unmocked_get_coin(self):
    #     # use envvar NUMISTA_KEY as api_key
    #    numistaClient = NumistaClient()
    #    result = numistaClient.get_coin(Consts.JSON_COIN.VIZSLA_ID)
    #    self.assertEqual(result['title'], '2000 Forint (Hungarian Vizsla)')
    #    import json
    #    self.assertJSONEqual(json.dumps(result), Consts.JSON_COIN.VIZSLA_TEXT)
    # endregion