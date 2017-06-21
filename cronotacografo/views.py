from rest_framework import viewsets
from .models import Registro
from .serializers import RegistroSerializer


class RegistroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    filter_fields = ('id', 'p', 'a', 'data')

    def get_queryset(self):
        queryset = Registro.objects.all()
        # import ipdb; ipdb.set_trace()
        data_gte = self.request.query_params.get('data_gte', None)
        if data_gte:
            queryset = queryset.filter(data__gte=data_gte)

        data_lte = self.request.query_params.get('data_lte', None)
        if data_lte:
            queryset = queryset.filter(data__lte=data_lte)

        return queryset
