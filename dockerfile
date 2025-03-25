# Imagem base Python
FROM python:3.10-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    NPM_BIN_PATH=/usr/bin/npm \
    NODE_ENV=production

# Instalar Node.js e npm (necessário para o Tailwind)
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Criar e definir diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o projeto
COPY . .

# Instalar e compilar o Tailwind CSS
WORKDIR /app/app
RUN python manage.py tailwind install
RUN python manage.py tailwind build

# Configurar o banco de dados
RUN python manage.py migrate

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Porta que a aplicação vai usar
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["gunicorn", "--chdir", "/app/app", "webapp.wsgi:application", "--bind", "0.0.0.0:8000"]