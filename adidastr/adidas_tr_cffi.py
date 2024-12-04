import requests

from curl_cffi import requests as cureq
from parsel import Selector

url = "https://www.adidas.com.tr/tr/erkek-ayakkabi?start=48"


resp = cureq.get(url, impersonate="chrome")



selector = Selector(resp.text)

#print(resp.text)
print(resp.status_code)
#shoes_name = selector.css("p::text").get()

#print(shoes_name)


# all shoes cards
product_cards = selector.css('footer[data-testid="product-card-details"]')

# create appending list
shoes = []

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