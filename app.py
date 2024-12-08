from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
#Iniciar Flask
app = Flask(__name__)
#construir as funcionalidades

CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/')
def homepage():
    tabela = pd.read_csv('cartas_tropa.csv')
    respostas = []
    for d in range(0, 72):
        resposta = {
            'id': str(tabela['ID'][d]),
            'carta': str(tabela['Carta'][d]),
            'tipo': str(tabela['Tipo'][d]),
            'raridade': str(tabela['Raridade'][d]),
            'elixir': str(tabela['Elixir'][d]),
            'vida': str(tabela['Vida'][d]),
            'dano': str(tabela['Dano'][d]),
            'velocidade_de_impacto': str(tabela['Velocidade de impacto'][d]),
            'alvo': str(tabela['Alvo'][d]),
            'alcance': str(tabela['Alcance'][d]),
            'velocidade': str(tabela['Velocidade'][d]),
            'unidades': str(tabela['Unidades'][d]),
            'especial': str(tabela['Especial'][d])
        }
        respostas.append(resposta.copy())
        resposta.clear()

    return jsonify(respostas)


#basicamente essa função relata em que link irá rodar está página


@app.route('/construcoes')
def construcoes():
    tabela = pd.read_csv('cartas_construcao.csv')
    construcoes = []
    construcao = {}
    for i in range(0, 12):
        construcao = {
            'id': str(tabela['ID'][i]),
            'carta': str(tabela['Carta'][i]),
            'elixir': str(tabela['Elixir'][i]),
            'vida': str(tabela['Vida'][i]),
            'tempo_de_invocacao': str(tabela['tempo por invocacao'][i]),
            'dano': str(tabela['Dano'][i]),
            'tipo': str(tabela['Tipo'][i]),
            'raridade': str(tabela['Raridade'][i]),
            'especial': str(tabela['Especial'][i])
        }
        construcoes.append(construcao.copy())
        construcao.clear()
    return jsonify(construcoes)


@app.route('/feitico')
def feitico():
    tabela = pd.read_csv('cartas_feitico.csv')
    feitico = {}
    feiticos = []
    for i in range(0, 19):
        feitico = {
            'id': str(tabela['ID'][i]),
            'carta': str(tabela['Carta'][i]),
            'elixir': str(tabela['Elixir'][i]),
            'raio': str(tabela['Raio'][i]),
            'dano_em_area': str(tabela['Dano em area'][i]),
            'dano_a_torre': str(tabela['Dano a torre'][i]),
            'tipo': str(tabela['Tipo'][i]),
            'raridade': str(tabela['Raridade'][i]),
            'especial': str(tabela['Especial'][i])
        }
        feiticos.append(feitico.copy())
        feitico.clear()
    return jsonify(feiticos)


@app.route('/contatos')
def contatos():
    return "Esse são os contatos"

if __name__ == '__main__':
    app.run()

#caso vocÊ estiver rodando em replit você precisa dentro do parenteses do desta maneira "app.run(host='0.0.0.0')"
