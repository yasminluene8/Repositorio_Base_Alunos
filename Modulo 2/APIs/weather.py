# Criar um código que consuma uma api de clima e informe 
# a temperatura e a descrição em um lugar especifíco

# 1. definir chave da API e o link da requisição
import requests

cidade = input("Digite o nome da cidade: ").strip()
api_key = "2a1ac38a32354cb7b19133643251408"
url = f"https://api.weatherapi.com/v1/current.json"

# 2. Parametros da requisição
parametros ={
    "key":api_key,
    "q":cidade,
    "lang":"pt" # Define a língua da resposta com português do Brasil
}

# 3. Fazer a requisiçaõ
resposta = requests.get(url, params=parametros)

# 4. Verificar se arequisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["current"]["temp_c"]
    descricao = dados["current"]["condition"]["text"]
    print(f"Temperatura na cidade {cidade} é {temperatura}°C.")
    print(f"Descrição: {descricao}")
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)