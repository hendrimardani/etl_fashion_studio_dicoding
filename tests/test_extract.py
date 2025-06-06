import unittest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
import requests
from utils.extract import fetching_content, extract_fashion_data, scrap_fashion

class TestExtract(unittest.TestCase):
    def setUp(self):
        self.url = "https://fashion-studio.dicoding.dev"

    @patch('requests.Session.get')
    def test_fetching_content_success(self, mock_get):
        """Test fetching_content() saat berhasil mengambil data."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body><h1>Test Page</h1></body></html>"
        mock_get.return_value = mock_response

        result = fetching_content(self.url)

        self.assertIsNotNone(result)
        self.assertIn(b"Test Page", result)


    @patch('requests.Session.get')
    def test_fetching_content_failure(self, mock_get):
        """Test fetching_content() saat terjadi kesalahan."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        result = fetching_content(self.url)
        self.assertIsNone(result)


    def test_extract_fashion_data(self):
        """Test extract_fashion_data() untuk mengambil informasi fashion dari elemen HTML."""
        # Buat hasil scrap palsu
        mock_html = '''
        <div class="collection-card">
            <div class="product-details">
                <h3>Cool Jacket</h3>
                <div class="price-container"><span>$99.99</span></div>
                <p>Rating: 4.5</p>
                <p>Colors: None</p>
                <p>Size: M</p>
                <p>Gender: Unisex</p>
            </div>
        </div>
        '''
        soup = BeautifulSoup(mock_html, "html.parser")
        card = soup.find('div', class_='collection-card')
        result = extract_fashion_data(card)

        expected_result = {
            "Title": "Cool Jacket",
            "Price": "$99.99",
            "Rating": "4.5",
            "Colors": None,
            "Size": "M",
            "Gender": "Unisex"
        }
        self.assertEqual(result, expected_result)


    @patch('requests.Session.get')
    def test_scrap_fashion(self, mock_get):
        """Test scrap_fashion() untuk memastikan fungsi berjalan dengan data mock."""
        # Buat hasil scrap palsu
        mock_html = '''
        <html>
            <body>
                <div class="collection-card">
                    <div class="product-details">
                        <h3>Cool Jacket</h3>
                        <div class="price-container"><span>$99.99</span></div>
                        <p>Rating: 4.5</p>
                        <p>Colors: Red, Blue</p>
                        <p>Size: M</p>
                        <p>Gender: Unisex</p>
                    </div>
                </div>
            </body>
        </html>
        '''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = mock_html.encode("utf-8")
        mock_get.return_value = mock_response

        result = scrap_fashion(start_page=1, delay=0)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Title"], "Cool Jacket")
