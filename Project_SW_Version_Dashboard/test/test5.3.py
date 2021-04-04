import requests
r = requests.get('http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
print(r)
print(r.headers)