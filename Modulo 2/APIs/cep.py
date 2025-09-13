# Instalar a biblioteca requests através do comando pip install requests (no terminal)
# Importar a biblioteca para o arquivo de trabalho

import requests

# Solicitar os dados da entrada
cep = input("Digite o cep (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json"

resposta = requests.get(url) # Aqui estamos fazendo uma requisição

if resposta.status_code == 200:
    dados = resposta.json()
    if "erro"not in dados:
        print(f"CEP: {dados["cep"]}")
        print(f"Logradouro:{dados["logradouro"]}")
        print(f"Cidade:{dados["localidade"]}")
        print(f"Estado:{dados["uf"]}")
    else:
        print("CEP não foi encontrado")
else:
    print(f"Erro na requisição: {resposta.status_code}.")
    print(resposta.content)