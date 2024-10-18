# scrape_agriverts.py

import requests
from bs4 import BeautifulSoup
import json

def scrape_agriverts_products():
    url = 'https://agriverts.com/products'  # Update if necessary
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []

    # Find all product sections
    product_sections = soup.find_all('div', {'data-ux': 'ContentBasic'})
    
    for section in product_sections:
        # Extract product title
        title_elem = section.find('h4', {'data-ux': 'ContentHeading'})
        title = title_elem.get_text(strip=True) if title_elem else 'No Title'

        # Extract product description
        desc_elem = section.find('div', {'data-ux': 'ContentText'})
        description = desc_elem.get_text(strip=True) if desc_elem else 'No Description'

        # Since there's no direct product URL in the snippet, we'll use the main URL
        product_url = url

        product = {
            'id': len(products) + 1,
            'title': title,
            'description': description,
            'location': 'Global',
            'production_type': ['vertical farming'],
            'solution_type': ['hydroponics'],
            'website': product_url
        }
        products.append(product)

    return products

if __name__ == '__main__':
    products = scrape_agriverts_products()
    # Save to JSON file
    with open('agriverts_products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)
    print(f"Scraped {len(products)} products from Agriverts.")