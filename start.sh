#!/bin/bash
# Apenas comandos para o ambiente de produção devem estar neste arquivo

# Inicie os processos do Gunicorn
echo Iniciando o Gunicorn
gunicorn mapa.wsgi:application \
    -k gevent \
    --bind 0.0.0.0:8000 \
    --workers 16
