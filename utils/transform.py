import pandas as pd
from datetime import datetime

def transform_to_DataFrame(data):
    """Mengubah data menjadi DataFrame."""
    df = pd.DataFrame(data)
    
    return df


def transform_data(data, exchange_rate):
    """Menggabungkan semua transformasi data menjadi satu fungsi."""
    try:
        data = data[~data["Title"].isin(['Unknown Product'])]
        data = data[~data["Price"].isin([None])]
        data = data[~data["Rating"].isin(['⭐ Invalid Rating'])]
        data["Rating"] = data["Rating"].str.lstrip('⭐').astype(float)
        data["Colors"] = data["Colors"].astype(int)
        data["Price"] = data["Price"].replace('\$', '', regex=True).astype(float)
        data["Price"] = data["Price"] * exchange_rate
        data["Timestamp"] = datetime.now()

        data.drop_duplicates(inplace=True)
        data.dropna(axis=1, inplace=True)
    except ValueError as e:
        print(f"An occured {e}")
        return None
    except TypeError as e:
        print(f"An occured {e}")
        return None

    return data
