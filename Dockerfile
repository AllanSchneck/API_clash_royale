# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie apenas o requirements.txt primeiro para otimizar o cache de dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para dentro do contêiner
COPY . .

# Exponha a porta que o Flask usará (a porta será configurada automaticamente pelo Fly.io)
EXPOSE 8080

# Defina a variável de ambiente FLASK_APP para que o Flask saiba qual arquivo executar
ENV FLASK_APP=apiclash.py

# Comando para rodar a aplicação Flask (ajustado para usar a variável de ambiente FLASK_APP)
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]