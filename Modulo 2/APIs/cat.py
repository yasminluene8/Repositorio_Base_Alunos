# API que apresenta curiosidades sobre os gatos

import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

print("Fato sobre gatos:", response.json()["fact"])