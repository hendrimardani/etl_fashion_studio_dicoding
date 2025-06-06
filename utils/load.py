import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os
import ast

def store_to_postgre(DataFrame):
    """Fungsi untuk menyimpan data ke dalam PostgreSQL."""
    DB_URL = "postgresql+psycopg2://hendri:hendri@localhost:5432/db_fashions"
    try:
        engine = create_engine(DB_URL)
        
        with engine.connect() as con:
            DataFrame.to_sql('fashionstoscrap', con=con, if_exists='append', index=False)
            print("Data berhasil ditambahkan!")
        
    except Exception as e:
        print(f"An error occured: {e}")
        

def store_to_csv(DataFrame):
    """Fungsi untuk menyimpan data ke dalam CSV."""
    DataFrame.to_csv("data_fashions.csv", index=False)


def store_to_google_sheet(DataFrame):
    """Fungsi untuk menyimpan data ke dalam Google Sheet."""
    load_dotenv(dotenv_path=".env_prod")

    SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
    # mengubah isi variabel environment yang berupa string menjadi list Python asli.
    SCOPES = ast.literal_eval(os.getenv("SCOPES"))
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        client = gspread.authorize(creds)
        sheet = client.open_by_key(SPREADSHEET_ID).worksheet("Sheet1")

        set_with_dataframe(sheet, DataFrame) 
        print("Berhasil menambahkan data!")
    except Exception as e:
         print(f"An error occurred: {e}")