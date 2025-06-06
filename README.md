# Features
- Scrap Data From Website https://fashion-studio.dicoding.dev
- Extract Data with Transform
- Load data into csv, google sheets, and postgresql
- Unit test for testing using pytest

# Usage
```bash
python -m venv .env
pip install -r requirements.txt

# Menjalankan skrip utama
python main.py

# Menjalankan unit test pada folder test
python -m pytest tests

# Menjalankan unit test pada folder tests dengan covarege report html
python -m pytest tests --cov --cov-report=html

# Menjalankan test coverage pada folder tests
coverage run -m pytest tests
```

# Folder Structure
```
📁 submission-pemda/
├── 📁 .env/
│   ├── 📁 Include/
│   └── 📁 Lib/
|   └── 📁 Scripts/
├── 📁 htmlcov/
├── 📁 tests/
│   ├── test_extract.py
│   ├── test_load.py
│   ├── test_transform.py
├── 📁 utils
│   ├── extract.py
│   ├── load.py
│   ├── transform.py
├── main.py
├── data_fashions.csv
└── submission.txt
```


# Store to CSV
![store_to_csv](https://github.com/user-attachments/assets/4bf56d37-513b-4344-a72a-cbdc9ca83d8e)

# Store to Goolge Sheets
![store_to_google_sheet](https://github.com/user-attachments/assets/1fb7d9e4-6af8-4883-b45f-8ad131e8d393)

# Store to Postgresql
![store_to_postgresql](https://github.com/user-attachments/assets/7945516f-9d12-4aca-bd11-20a1e7e389c4)

# Unit Test using Pytest
![unit_test](https://github.com/user-attachments/assets/40bc8be6-bb35-4a30-af9a-aa7d21c6831f)
