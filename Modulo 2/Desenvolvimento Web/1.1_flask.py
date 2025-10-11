# No terminal instalar o flask com o comando : pip install flask
# Exercicio 1.1: Hello Flask
# Criar um app Flask básico que exibe "Olá, mundo" na rota principal ('/)

from flask import Flask
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') #@decorador de função
def home():
    return "Olá Mundo!"

if __name__ == '__main__':
    app.run(debug=True)

