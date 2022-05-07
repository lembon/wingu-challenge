from rest_framework import serializers
from .models import Reclamo

class ReclamoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reclamo
        fields = ('id', 'titulo', 'descripcion', 'comuna', 'imagen')