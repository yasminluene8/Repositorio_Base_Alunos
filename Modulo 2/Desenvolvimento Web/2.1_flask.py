# Exercício 2:1: HTML básico na resposta
# Modificar sua rota principal para retornar um pequeno html com título,
# parágrafo e um link para renderizar um arquivo .html
# Usar 'rende_template' para renderizar um arquivo .html
# Usar 'url_for() nas anchor tags do scrip html

from flask import Flask, render_template
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/') # Rota principal , que é a rota index('/')
def home():
    return render_template('ex_2-1.html') # A biblioteca render_template "lê" o html

@app.route('/sobre') # Nova rota
def sobre():
    return "Fabrica de Programadores"

@app.route('/zezinho') # Nova rota
def zezinho():
    return 'Achou anota'

if __name__=='__main__':
    app.run(debug=True)
