from flask import Flask, render_template, request
import random

app = Flask(__name__)

tentativas_restantes = 10
numero_aleatorio = random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def jogo_adivinhacao():
    global tentativas_restantes, numero_aleatorio
    mensagem = ''
    reiniciar = False

    if tentativas_restantes > 0:
        if request.method == 'POST':
            tentativa = int(request.form['tentativa'])
            if tentativa < numero_aleatorio:
                mensagem = 'Tente um número maior.'
            elif tentativa > numero_aleatorio:
                mensagem = 'Tente um número menor.'
            else:
                mensagem = 'Parabéns! Você adivinhou o número.'
                tentativas_restantes = 0  # Zera as tentativas
                reiniciar = True

        tentativas_restantes -= 1
    else:
        mensagem = 'Você usou todas as tentativas. O número correto era: ' + str(numero_aleatorio)
        reiniciar = True

    if reiniciar:
        numero_aleatorio = random.randint(1, 100)
        tentativas_restantes = 10

    return render_template('index.html', mensagem=mensagem, tentativas_restantes=tentativas_restantes, numero_aleatorio=numero_aleatorio)

if __name__ == '__main__':
    app.run(debug=True)