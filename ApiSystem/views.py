from rest_framework import viewsets, permissions
from ApiSystem.serializers import PortasSerializer

from HardwareApp.models import Portas

# Create your views here.
#Inserir a Views de Cada API que será Utilizada.
class PortasViewSet(viewsets.ModelViewSet):
    queryset = Portas.objects.all().order_by('Nome')
    serializer_class = PortasSerializer
    #permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        portasaplication = super().get_queryset()
        return portasaplication
