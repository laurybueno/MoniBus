#!/bin/bash
# Apenas comandos para o ambiente de produção devem estar neste arquivo

# Inicie os processos do Gunicorn
echo Iniciando o Gunicorn
exec gunicorn mapa.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
