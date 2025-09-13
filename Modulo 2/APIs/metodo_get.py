# Método GET utiizando uma api de teste
# Esse método busca (get) alguma informação/coisa
import requests
url = "https://jsonplaceholder.typicode.com/posts/5"
response = requests.get(url)

print("Status:", response.status_code)
print("Titulo do post:",response.json()["title"])