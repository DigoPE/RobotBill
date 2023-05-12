from rest_framework import serializers
from HardwareApp.models import Portas, Placas


# ------ serializers de controle de Dados do DB ----------------
class PortasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portas
        fields = ['Nome', 'Descricao']

class PlacasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placas
        fields = ['Nome', 'Descricao', 'Porta']

# ------ FIM  ------------------------------------------------

# ------ serializers de controle de Arduino ----------------
class FarolSerializer(serializers.Serializer):
    ordem = serializers.CharField()

class TestaPortasSerializer(serializers.Serializer):
    nome = serializers.CharField()
    status = serializers.CharField()
# ------ FIM  ----------------------------------------------------