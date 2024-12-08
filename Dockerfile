# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código e arquivos necessários para o contêiner
COPY . .

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "apiclash.py"]
