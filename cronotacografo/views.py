from rest_framework import viewsets
from .models import Registro
from .serializers import RegistroSerializer


class RegistroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
