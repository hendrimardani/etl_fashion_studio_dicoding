import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import store_to_postgre, store_to_csv

class TestStoreToPostgre(unittest.TestCase):
    def setUp(self):
        # Buat DataFrame palsu
        self.mock_df = pd.DataFrame({
            "Title": ["T-Shirt 2", "Hoodie 3"],
            "Price": [163440.0, 7950080.0],
            "Rating": [3.9, 4.8],
            "Colors": [3, 3],
            "Size": ["M", "L",],
            "Gender": ["Women", "Unisex"],
            "Timestamp": ["2025-03-01 08:44:49.548384", "2025-03-01 08:44:49.548384"]
        })


    @patch('sqlalchemy.create_engine')  # Mock create_engine
    def test_store_to_postgre_success(self, mock_create_engine):
        """Test jika data berhasil disimpan tanpa error."""
        # Buat mock engine
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        
        # Buat mock connection
        mock_connection = MagicMock()
        mock_engine.connect.return_value.__enter__.return_value = mock_connection

        # Pastikan objek connection memiliki method `to_sql()`
        mock_connection.to_sql = MagicMock()

        # Panggil fungsi dengan mock
        result = store_to_postgre(self.mock_df)
        self.assertIsNone(result)  # Pastikan fungsi mengembalikan None jika sukses


    @patch('sqlalchemy.create_engine')
    def test_store_to_postgre_exception(self, mock_create_engine):
        """Test jika terjadi error dalam koneksi database."""
        mock_create_engine.side_effect = Exception("Database connection failed")  # Simulasi error

        # Panggil fungsi dengan mock
        result = store_to_postgre(self.mock_df)

        # Pastikan fungsi menangani error dengan mengembalikan None
        self.assertIsNone(result)

    
    @patch.object(pd.DataFrame, 'to_csv')  # Mock metode to_csv dari DataFrame
    def test_store_to_csv_success(self, mock_to_csv):
        """Test jika data berhasil disimpan ke CSV tanpa error."""
        # Panggil fungsi
        store_to_csv(self.mock_df)

        # **Pastikan `to_csv()` dipanggil dengan benar**
        mock_to_csv.assert_called_once_with("data_fashions.csv", index=False)