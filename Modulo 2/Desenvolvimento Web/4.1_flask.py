# Exercício 4.1: formulario simples com request form
# Crie uma paina com um formulario que envie um nome e
# retorna uma saudação personalizada com esse nome


from flask import Flask, render_template, request
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/', methods=['POST','GET'])
def index():
    if request . method == 'POST':
        nome = request.form['nome']
        return f'Olá {nome}! Seja, bem vindo (a) a Fábrica de Programadores.'
    return render_template('ex_4-1.html')


if __name__=='__main__':
    app.run(debug=True)

