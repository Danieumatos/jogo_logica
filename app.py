from flask import Flask, render_template, request, redirect, url_for
from licoes import LICOES
from desafios import DESAFIOS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instrucoes')
def instrucoes():
    return render_template('instrucoes.html')

@app.route('/licao/<int:nivel>')
def licao(nivel):
    licao = LICOES[nivel]
    return render_template('licao.html', licao=licao, nivel=nivel)

@app.route('/verificar_licao', methods=['POST'])
def verificar_licao():
    codigo = request.form['codigo']
    nivel = int(request.form['nivel'])
    ambiente = {}
    try:
        exec(codigo, ambiente)
        resultado = eval(LICOES[nivel]['teste'], ambiente)
        if resultado:
            mensagem = "Parabéns! Você concluiu a lição."
            return render_template('licao.html', licao=LICOES[nivel], nivel=nivel, mensagem=mensagem)
        else:
            erro_mensagem = "Erro: Sua solução não está correta."
            return render_template('licao.html', licao=LICOES[nivel], nivel=nivel, erro_mensagem=erro_mensagem)
    except Exception as e:
        erro_mensagem = f"Erro encontrado: {e}"
        return render_template('licao.html', licao=LICOES[nivel], nivel=nivel, erro_mensagem=erro_mensagem)

@app.route('/desafio/<dificuldade>/<int:nivel>')
def desafio(dificuldade, nivel):
    desafio = DESAFIOS[dificuldade][nivel]
    return render_template('desafio.html', desafio=desafio, dificuldade=dificuldade, nivel=nivel)

@app.route('/verificar_desafio', methods=['POST'])
def verificar_desafio():
    codigo = request.form['codigo']
    dificuldade = request.form['dificuldade']
    nivel = int(request.form['nivel'])
    ambiente = {}
    try:
        exec(codigo, ambiente)
        resultado = eval(DESAFIOS[dificuldade][nivel]['teste'], ambiente)
        if resultado:
            mensagem = "Parabéns! Você concluiu o desafio."
            return render_template('desafio.html', desafio=DESAFIOS[dificuldade][nivel], dificuldade=dificuldade, nivel=nivel, mensagem=mensagem)
        else:
            erro_mensagem = "Erro: Sua solução não está correta."
            return render_template('desafio.html', desafio=DESAFIOS[dificuldade][nivel], dificuldade=dificuldade, nivel=nivel, erro_mensagem=erro_mensagem)
    except Exception as e:
        erro_mensagem = f"Erro encontrado: {e}"
        return render_template('desafio.html', desafio=DESAFIOS[dificuldade][nivel], dificuldade=dificuldade, nivel=nivel, erro_mensagem=erro_mensagem)

@app.route('/dica/<int:nivel>')
def dica_licao(nivel):
    dica = LICOES[nivel].get('dica', 'Nenhuma dica disponível para esta lição.')
    return dica

@app.route('/dica_desafio/<dificuldade>/<int:nivel>')
def dica_desafio(dificuldade, nivel):
    dica = DESAFIOS[dificuldade][nivel].get('dica', 'Nenhuma dica disponível para este desafio.')
    return dica

if __name__ == '__main__':
    app.run(debug=True)
