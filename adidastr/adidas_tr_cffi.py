import requests
import sqlite3
from curl_cffi import requests as cureq
from parsel import Selector

base_url = "https://www.adidas.com.tr/tr/erkek-ayakkabi"

shoes = []

for start in range(0,673,48):

    # create ulr

    url = f"{base_url}?start={start}"
    print(f"data incoming:{url}")
    resp = cureq.get(url, impersonate="chrome")

    selector = Selector(resp.text)

    #print(resp.text)
    print(resp.status_code)
    #shoes_name = selector.css("p::text").get()

    #print(shoes_name)


    # all shoes cards
    product_cards = selector.css('footer[data-testid="product-card-details"]')

    # create appending list

    for card in product_cards:
        
        price = card.css('div[data-testid="primary-price"]::text').get()
        
        name = card.css('p[data-testid="product-card-title"]::text').get()
        
        subtitle = card.css('p[data-testid="product-card-subtitle"]::text').get()
        
        colors = card.css('p[data-testid="product-card-colours"]::text').get()

        
        shoes.append({
            'name': name,
            'price': price,
            'subtitle': subtitle,
            'colors': colors
        })

# print information
for shoe in shoes:
    print(shoe)

def format_shoes(shoes):
    formatted_shoes = [
    
            (shoe['name'], shoe['price'], shoe['subtitle'], 
             shoe['colors'] if shoe['colors'] is not None else "NONE") for shoe in shoes]
    return formatted_shoes


def createdb(shoes):




    conn = sqlite3.connect("Adidastr.db")

    # Cursor
    cursor = conn.cursor()

    # Create Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        subtitle TEXT ,
        color TEXT 
    )
    """)

    print("Table was created")

    cursor.executemany("""
    INSERT INTO shoes (name, price, subtitle, color) 
    VALUES (?, ?, ?, ?)
    """, shoes)

    print("Values were entered")

    # save and close
    conn.commit()
    conn.close()

    print("exited db.")

createdb(format_shoes(shoes))
