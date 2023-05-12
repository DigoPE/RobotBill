from rest_framework import viewsets, permissions
from ApiSystem.serializers import PortasSerializer, PlacasSerializer

from HardwareApp.models import Portas, Placas
from Arduino.ControlaFarolApi import Farol
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from util.Info_System import Informacao_System

# Create your views here.
#Inserir a Views de Cada API que será Utilizada.
class PortasViewSet(viewsets.ModelViewSet):
    queryset = Portas.objects.all().order_by('Nome')
    serializer_class = PortasSerializer
    #permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        portasaplication = super().get_queryset()
        return portasaplication

class PlacasViewSet(viewsets.ModelViewSet):
    queryset = Placas.objects.all().order_by('Nome')
    serializer_class = PlacasSerializer
    #permission_classes = [permissions.IsAuthenticated,]

    def get_queryset(self):
        placasaplication = super().get_queryset()
        return placasaplication

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

class TestaPortasViewSet():
    @staticmethod
    @csrf_exempt
    def testPortas(request):
        nomes_portas = []
        if request.method == 'POST':
            resultado_portas = Informacao_System.get_testaPortas('self')
            for porta in resultado_portas:
                nome_porta = porta[0]
                status_porta = porta[1]
                nomes_portas.append({'nome': nome_porta, 'status_porta': status_porta})

            return JsonResponse({'nomes_portas': nomes_portas})
        else:
            return JsonResponse({'nomes_portas': 'error', 'message': 'Invalid request method'})