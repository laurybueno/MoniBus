from django.core.management.base import BaseCommand
from cronotacografo.models import Registro
import json
import os
import requests
import datetime
import warnings


class Command(BaseCommand):
    help = 'Recebe dados geográficos de ônibus minuto a minuto da API Olho Vivo da SPTrans'

    url = 'http://api.olhovivo.sptrans.com.br/v2.1'
    s = requests.session()

    def renew_token(self):
        self.s.post(self.url + '/Login/Autenticar?token=' + os.getenv('API_KEY'), timeout=10)

    # Returns json text ready to be saved as file
    def get_posicao(self):
        try:
            res = self.s.get(self.url + '/Posicao', timeout=30)
            return res.text
        except Exception:
            return ''

    def handle(self, *args, **options):

        self.renew_token()
        data = json.loads(self.get_posicao())

        # Para cada linha retornada
        for linha in data['l']:
            cLinha = linha['c']
            codigoLinha = linha['cl']
            sentidoLinha = linha['sl']

            # Para cada veículo nessa linha
            for veiculo in linha['vs']:
                reg = Registro()
                reg.posicao = "POINT(" + str(veiculo['px']) + " " + str(veiculo['py']) + ")"
                reg.prefixo = veiculo['p']
                reg.acessivel = bool(veiculo['a'])
                reg.hr = str(data['hr'])
                reg.codigoLinha = codigoLinha
                reg.linha = cLinha
                reg.sentidoLinha = sentidoLinha
                reg.save()
