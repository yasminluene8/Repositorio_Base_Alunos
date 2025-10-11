# Exercício 2.2: Links entre rotas
# Adicionar um menu de navegação simples com links para todas as rotas(/',/sobre,/saudacao,etc.)
# Passar a variavel através do 'url_for'
# Dentro do script html: ("{{url_for('saudacao'), nome='Joãozinho'}}")
# 'saudacao' é o nome da função Python que define a rota
# nome= 'Joãozinho' está passando o valor para a variável que a rota espera (<nome>) 

from flask import Flask, render_template
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') # @decorador de função
def home():
    return render_template('ex_2-2.html')

@app.route('/sobre') # 
def sobre():
    return "Olá , eu sou aluno do projeto Fábrica de Programadores"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá {nome}! Seja bem-vindo(a)!'

@app.route('/dobro/<int:numero>') 
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}.'

if __name__=='__main__':
    app.run(debug=True)
