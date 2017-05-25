from django.contrib.gis.db import models


class Registro(models.Model):
    posicao = models.GeometryField(srid=4326,
                                   geography=False,
                                   )
    p = models.IntegerField('Veículo')
    a = models.NullBooleanField()
    data = models.DateTimeField('Hora do registro')
    hr = models.CharField('Hora da SPTrans', max_length=5)
    codigoLinha = models.IntegerField('Código da Linha')
