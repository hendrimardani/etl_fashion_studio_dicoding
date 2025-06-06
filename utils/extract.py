import requests
import time
from bs4 import BeautifulSoup
from utils.transform import transform_to_DataFrame, transform_data

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    )
}

def fetching_content(url):
    """Mengambil konten HTML dari URL yang diberikan."""
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    try:
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None
    except Exception as e:
        print(f"An error occured during scraping: {e}")
        return None


def extract_fashion_data(card):
    """Mengambil data fashion berupa nama, harga, rating, warna dan ukuran dari fashion (element html)."""
    div_product_details = card.find('div', class_='product-details')
    title = div_product_details.find('h3').text

    div_price_container = div_product_details.find('div', class_='price-container')
    price = div_product_details.find('span').text if div_price_container else None
    
    p_tags = div_product_details.find_all('p')

    rating = None
    colors = None
    size = None
    gender = None

    for p in p_tags:
        text = p.text.strip()
        if text.startswith("Rating:"):
            rating = text.replace("Rating:", "").strip().split("/")[0]  
        elif text.endswith("Colors"):
            colors = text.replace("Colors", "").strip().split(",")[0]
        elif text.startswith("Size:"):
            size = text.replace("Size:", "").strip()
        elif text.startswith("Gender:"):
            gender = text.replace("Gender:", "").strip()

    fashions = {
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Colors": colors,
        "Size": size,
        "Gender": gender
    }
    return fashions


def scrap_fashion(start_page=1, delay=2):
    """Fungsi utama untuk mengambil keseluruhan data, mulai dari requests hingga menyimpannya dalam variabel data."""
    data = []
    url = ""
    page_number = start_page
    is_first_page = True    
    while True:
        if is_first_page:
            BASE_URL = 'https://fashion-studio.dicoding.dev'
            url = BASE_URL
        else:
            BASE_URL = 'https://fashion-studio.dicoding.dev/page{}'
            url = BASE_URL.format(page_number)
        print(f"Scraping halaman: {url}")

        try:
            content = fetching_content(url)
            soup = BeautifulSoup(content, "html.parser")
            div_collection_card = soup.find_all('div', class_='collection-card')
            for item in div_collection_card:
                fashion = extract_fashion_data(item)
                data.append(fashion)

            is_first_page = False
            next_button = soup.find('li', class_='page-item next')
            if next_button:
                page_number += 1
                # time.sleep(delay) 
            else:
                break
        except requests.exceptions.RequestException as e:
            print(f"Error fetching website: {e}")
            return None
        except Exception as e:
            print(f"An error occured during scraping: {e}")
            return None
        
    return data