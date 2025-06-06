import unittest
import pandas as pd
import os 
from unittest.mock import patch
from utils.transform import transform_data

class TestTransform(unittest.TestCase):
    def setUp(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.url = f"{script_dir}/data_fashions.csv"
        self.exchange_rate = 16000
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

    @patch('pandas.read_csv')
    def test_transform_data_success(self, mock_read_csv):
        """Test transform_data() untuk mengecek apakah data yang dikembalikan sesuai (DataFrame)"""
        num_data = self.mock_df.shape[0]        
        # Atur return value dari mock
        mock_read_csv.return_value = self.mock_df
        # Panggil pd.read_csv (akan menggunakan mock)
        result = pd.read_csv(self.url)
        # Pastikan hasilnya sesuai dengan mock_df
        pd.testing.assert_frame_equal(result, self.mock_df)
        # Pastikan jumlah data sesuai
        self.assertEqual(result.shape[0], num_data)


    @patch('pandas.DataFrame')  # Mock DataFrame Pandas
    def test_value_error(self, mock_df):
        """Test jika terjadi ValueError dalam transformasi data."""
        mock_df.__getitem__.side_effect = ValueError("Invalid value conversion") 
        result = transform_data(mock_df, self.exchange_rate) 
        self.assertIsNone(result)  
        

    @patch('pandas.DataFrame')
    def test_type_error(self, mock_df):
        """Test jika terjadi TypeError dalam transformasi data."""
        mock_df.__getitem__.side_effect = TypeError("Type mismatch error")  
        result = transform_data(mock_df, self.exchange_rate)
        self.assertIsNone(result)


