# Exercício 1.4: Rota com número (tipagem de rota)
# Cria uma rota /dobrop/<int:numero> que recebe um número e recebe o dobro dele)

from flask import Flask
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') # @decorador de função
def home():
    return "Olá Mundo!"


@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Yasmim e sou uma estudante.'

@app.route('/saudacao/<nome>')
def saudaucao (nome):
    return f'Olá {nome}! Seja bem- vindo(a)!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}.'




if __name__ == '__main__':
    app.run(debug=True)
