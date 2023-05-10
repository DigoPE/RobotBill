from rest_framework import serializers
from HardwareApp.models import Portas


class PortasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portas
        fields = ['Nome', 'Descricao']
