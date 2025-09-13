#  Método PATCH ( atualização parcial)

import requests
url = "https://jsonplaceholder.typicode.com/posts/7"

atualizacao = {
    "title":"Título atualizado no exercício"
}
# Criando a requisição
response = requests.patch(url, json=atualizacao)

print("Status Code:", response.status_code)
print("Resposta da API:", response.json())