# Exercício 1.2: Rota personalizada
# Adicione uma nova rota ' /sobre' que retorna uma mensagem com o seu nome uma frase sobre você


from flask import Flask
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') #@decorador de função
def home():
    return "Olá Mundo!"


@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Yasmim e sou uma estudante.'








if __name__ == '__main__':
    app.run(debug=True)
