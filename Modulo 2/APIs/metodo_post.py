# Método POST ( adicionar /criar)

import requests
url = "https://jsonplaceholder.typicode.com/posts"

novo_post= {
    "title":"Meu primeiro POST",
    "body":"Estou apredendo a enviar dados com Python",
    "userid": 10
}
# Criando a requisição
response = requests.post(url, json=novo_post)

print("Status Code: ", response.status_code)
print("Resposta sa API: ", response.json())