from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/', methods= ['POST','GET'])
def index():
    # Se a requuisição for POST, o usuário enviou o formulário
    if request.method == 'POST':
        try:
            # 1. Capturara a opção e o número do formulário
            opcao = request.form['opcao']
            num = float(request.form['num'])
            resultado = None

            # 2. Lógica de cáculo
            if opcao == 'potenciacao' :
                resultado = num ** 2
            elif opcao == 'radiciacao':
                if num < 0:
                    erro = 'Não é possível calcular a raíz quadrada de um número negativo.'
                    return render_template('index.html', erro=erro)
                resultado = num ** 0.5
            return render_template('index.html', resultado =resultado, opcao_escolhida=opcao)
        except ValueError:
            erro = 'Por favor , digite apenas números válidos. '
            return render_template('index.html', erro=erro)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)