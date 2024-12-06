# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos da aplicação para dentro do container
COPY . .

# Instale as dependências
RUN pip install -r requirements.txt

# Exponha a porta necessária (se houver)
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "apiclash.py"]

CMD ["flyctl launch plan propose --manifest-path /tmp/manifest.json --region gig --copy-config"]
