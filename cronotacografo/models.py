from django.contrib.gis.db import models


class Registro(models.Model):
    posicao = models.GeometryField(srid=4326,
                                   geography=False,
                                   )
    prefixo = models.IntegerField('Veículo')
    acessivel = models.NullBooleanField()
    data = models.DateTimeField('Hora do registro', auto_now_add=True, db_index=True)
    hr = models.CharField('Hora da SPTrans', max_length=5)
    codigoLinha = models.IntegerField('Código da Linha', db_index=True)
    sentidoLinha = models.IntegerField('Sentido da Linha')
    linha = models.CharField('Código público da Linha', max_length=10, db_index=True)
