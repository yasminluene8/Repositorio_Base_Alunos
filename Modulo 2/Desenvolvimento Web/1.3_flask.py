# Exercício 1.3: Parametros na url (rotas dinânmicas)
# Cire uma rota /saudacao/<nome> que retorne "Olá, <nome>! Seja bem - vindo!"

from flask import Flask
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') #@decorador de função
def home():
    return "Olá Mundo!"


@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Yasmim e sou uma estudante.'

@app.route('/saudacao/<nome>')
def saudaucao (nome):
    return f'Olá {nome}! Seja bem- vindo(a)!'






if __name__ == '__main__':
    app.run(debug=True)
