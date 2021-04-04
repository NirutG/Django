# Source : https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
import requests
r = requests.get('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
print(r.text)