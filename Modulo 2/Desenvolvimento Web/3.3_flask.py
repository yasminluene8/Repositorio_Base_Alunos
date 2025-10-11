# Exercício 3.3: Condicionais em templates
# Crie uma rota que envia uma idade e, no template, use if para mostrar uma mensagem
# diferente se for maior de idade ou menor de idade

from flask import Flask, render_template
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') # @decorador de função
def index():
    return 'Hello Flask'

@app.route('/sobre') 
def sobre():
    return "Olá , eu sou aluno do projeto Fábrica de Programadores"

@app.route('/idade/<int:idade>')
def idade(idade):
    return render_template('ex_3-3.html',idade= idade)

if __name__=='__main__':
    app.run(debug=True)

