# Etapa 1: Build
FROM python:3.10-slim AS builder

# Variáveis de ambiente ESSENCIAIS para instalação de devDependencies
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    NODE_ENV=development \
    NPM_BIN_PATH=/usr/bin/npm

WORKDIR /app

# Instalar dependências de sistema e Node.js
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    git \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar o projeto
COPY . .

# Instalar dependências do Node.js (INCLUINDO devDependencies) e compilar Tailwind
WORKDIR /app/app/theme/static_src  
RUN npm install --include=dev && npm run build


WORKDIR /app/app 

# Comandos do Django
RUN python manage.py migrate && python manage.py collectstatic --noinput


# Etapa 2: Imagem final de produção
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    NODE_ENV=production 

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && pip install gunicorn

# Copiar apenas o necessário do builder
COPY --from=builder /app /app

EXPOSE 8000

CMD ["gunicorn", "--chdir", "/app/app", "webapp.wsgi:application", "--bind", "0.0.0.0:8000"]