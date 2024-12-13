# API clash royale

## 🚀 

Este é um projeto de api clash royale com endpoints get que contém detalhes mínimos sobre cada carta de clash royale
somente para estudos

### 📋 Pré-requisitos

Flask==2.3.0
Flask-CORS==5.0.0
pandas==2.1.0
gunicorn==20.1.0
numpy==1.26.4

### 🔧 Instalação
Utilizei render.com uma plataforma gratuita e junto com um documento Procfile consegui inicializar minha aplicação flask

exemplos
Procfile
web: gunicorn app:app


## ⚙️ Executando os testes

A api tem apenas três endpoint do tipo get
Tropa ) https://api-clash-royale.onrender.com/
Construções ) https://api-clash-royale.onrender.com/construcoes
Feitiço ) https://api-clash-royale.onrender.com/feitico

criei desta forma por conta que assim eu consigo organizar as tropas pelo tipo exatamente como está no jogo

### 🔩 Analise os testes de ponta a ponta

Estes testes consultam os pontos get podendo inspecionar os erros pelo javascript ou pelo render

## 🛠️ Construído com Python

Mencione as ferramentas que você usou para criar seu projeto

* [Flask](https://flask.palletsprojects.com/en/stable/changes/) - O framework web usado
* [Flask_cors](https://pypi.org/project/Flask-Cors/) - Utilizada para configuração cors
* [pandas]([https://rometools.github.io/rome/](https://pandas.pydata.org/)) - Usado para abrir arquivos CSV
* [numpy](https://numpy.org/) - Usado para resolver erros com binários


## ✒️ Autor

 [Allan Richard da Silva Schneck](https://github.com/AllanSchneck)


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](https://github.com/AllanSchneck/API_clash_royale/blob/API_clashV1.01/LICENSE.txt)) para detalhes.

