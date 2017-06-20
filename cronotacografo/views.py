import django_filters
from django.db import models
from rest_framework import viewsets, filters
from .models import Registro
from .serializers import RegistroSerializer


class TimeFilter(filters.FilterSet):
    class Meta:
        model = Registro
        fields = {
            'data': ('lte', 'gte'),
            'p': (),
        }

    filter_overrides = {
        models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }


class RegistroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    filter_fields = ('id', 'p', 'a', 'data')
    # filter_class = TimeFilter
