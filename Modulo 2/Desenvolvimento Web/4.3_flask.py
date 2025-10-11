# Exercício 4.3: Validação básica de campos
# Implementar uma verificação no formulário anterior 
# para garantir que os valores sejam números antes de soma - lós

from flask import Flask, render_template, request
app = Flask(__name__) # Representa o nome do arquivo

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            resultado = num1 + num2
            return render_template('ex_4-3.html', resultado=resultado)
        except:
            erro = 'Por favor, digite apenas números válidos.'
            return render_template('ex_4-3.html',erro=erro)
    return render_template('ex_4-3.html')

if __name__=='__main__':
    app.run(debug=True)

