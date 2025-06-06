from utils.extract import scrap_fashion
from utils.transform import transform_to_DataFrame, transform_data
from utils.load import store_to_csv, store_to_postgre, store_to_google_sheet

def main():
    """Fungsi utama untuk keseluruhan proses scraping hingga menyimpannya."""
    EXCHANGE_RATE = 16000
    
    all_fashions_data = scrap_fashion()
    if all_fashions_data:
        DataFrame = transform_to_DataFrame(all_fashions_data)
        DataFrame = transform_data(DataFrame, EXCHANGE_RATE)
        store_to_csv(DataFrame)
        store_to_postgre(DataFrame)
        store_to_google_sheet(DataFrame)
    else:
        print("Tidak ada data yang ditemukan.") 
 
if __name__ == '__main__':
    main()