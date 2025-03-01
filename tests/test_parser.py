from src.parser import HeadHunterAPI

from unittest import TestCase
from unittest.mock import patch


class TestGetDataFromApi(TestCase):
    @patch('requests.get')
    def test_get_data(self, mock_get):
        hh = HeadHunterAPI()
        mock_get.return_value.json.return_value = {
            "items": [{"name": "test_vac", "desc": "test_vac"}, {"name": "test_vac2", "desc": "test_vac2"}]}
        hh.load_vacancies("test")
        assert hh.vacancies == [{"name": "test_vac", "desc": "test_vac"}, {"name": "test_vac2", "desc": "test_vac2"},
                               {"name": "test_vac", "desc": "test_vac"}, {"name": "test_vac2", "desc": "test_vac2"}]
        mock_get.assert_called_with(hh.url, params=hh.params, headers=hh.headers)
