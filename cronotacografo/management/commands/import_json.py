from django.core.management.base import BaseCommand
from cronotacografo.models import Registro
import json
import os
import datetime
import re
import warnings


class Command(BaseCommand):
    help = 'Importa todos os arquivos JSON encontrados no diretório para o banco de dados. Certifique-se de ter apenas JSONs válidos nesse caminho'

    def add_arguments(self, parser):
        parser.add_argument('json_path', nargs='+', type=str)

    def handle(self, *args, **options):
        json_path = options['json_path'][0].rstrip('/')  # remove a trailing slash, if any
        files = []
        for (dirpath, dirnames, filenames) in os.walk(json_path):
            [files.append(dirpath + "/" + filename) for filename in filenames if ".json" in filename]

        count = 0
        files_scanned = 0
        warnings.filterwarnings("ignore")  # ignore timezone warnings
        try:
            for index, json_file in enumerate(files):
                with open(json_file) as f:
                    files_scanned += 1
                    try:
                        arquivo = json.load(f)
                        arquivo['meta'] = json_file[:-5].split('-')
                    except Exception as e:
                        print(e)
                        continue

                for vs in arquivo['vs']:
                    reg = Registro()
                    reg.posicao = "POINT(" + str(vs['px']) + " " + str(vs['py']) + ")"
                    reg.p = vs['p']
                    reg.a = bool(vs['a'])
                    reg.data = datetime.datetime.fromtimestamp(float(arquivo['meta'][1]))
                    reg.hr = str(arquivo['hr'])
                    reg.codigoLinha = re.match('.*?([0-9]+)$', arquivo['meta'][0]).group(1)
                    reg.save()
                    count += 1
                if index % 10 == 0:
                    print(str(datetime.datetime.now()))
                    print('Arquivos lidos: ' + str(index))
                    print('Arquivos no total: ' + str(len(files)) + '\n')
        except Exception as e:
            print(e)

        print('Arquivos lidos: ' + str(files_scanned))
        print('Veículos processados: ' + str(count))
