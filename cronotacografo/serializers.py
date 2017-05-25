from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Registro


class RegistroSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Registro
        geo_field = "posicao"

        fields = '__all__'
