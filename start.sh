#!/bin/bash
# Apenas comandos para o ambiente de produção devem estar neste arquivo

# Migre o banco de dados, se necessário
python manage.py migrate

# Inicie os processos do Gunicorn
echo Iniciando o Gunicorn
gunicorn mapa.wsgi:application \
    -k gevent \
    --bind 0.0.0.0:8000 \
    --workers 16 \
    --timeout 3600
