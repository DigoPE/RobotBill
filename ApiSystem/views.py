from rest_framework import viewsets, permissions
from ApiSystem.serializers import PortasSerializer

from HardwareApp.models import Portas
from Arduino.ControlaFarolApi import Farol
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#Inserir a Views de Cada API que será Utilizada.
class PortasViewSet(viewsets.ModelViewSet):
    queryset = Portas.objects.all().order_by('Nome')
    serializer_class = PortasSerializer
    #permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        portasaplication = super().get_queryset()
        return portasaplication


class FarolViewSet():
    @staticmethod
    @csrf_exempt
    def farol(request):
        #if request.method == 'POST':
        if request.method == 'GET':
            ordem = request.GET.get('ordem')
            Farol.ComandaFarol(ordem)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
