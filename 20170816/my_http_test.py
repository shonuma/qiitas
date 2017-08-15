# python 3.5.2

from unittest.mock import MagicMock, patch

import pytest

import my_http


class TestGetStatusCode:
    @pytest.fixture
    def url(self):
        return 'http://example.com'

    @pytest.mark.skip
    def test_online(self, url):
        assert my_http.get_status_code(url) == 200

    def test_offline(self, url):
        with patch('my_http.requests') as mock_requests:
            mock_response = MagicMock(status_code=200)
            mock_requests.get.return_value = mock_response

            assert my_http.get_status_code(url) == 200

    def test_client_error(self, url):
        with patch('my_http.requests') as mock_requests:
            mock_response = MagicMock(status_code=400)
            mock_requests.get.return_value = mock_response

            assert my_http.get_status_code(url) == 400

    def test_server_error(self, url):
        with patch('my_http.requests') as mock_requests:
            mock_response = MagicMock(status_code=500)
            mock_requests.get.return_value = mock_response

            assert my_http.get_status_code(url) == 500
