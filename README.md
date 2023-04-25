# Robo Bill
 Esse projeto vai realizar toda a comunicação de interação do Robô Bill através de API do ChatGPT.
Além de toda a interação com o hardware Arduino.


# Instalando pacotes para rodar o ChatGPT:

1) - Instale o Django e o TensorFlow:
- pip install django tensorflow
- pip install openai

2) - Crie um novo projeto Django:
- django-admin startproject chatgpt_api

3) - Entre no projeto e crie uma nova aplicação:
   - cd chatgpt_api
   - python manage.py startapp chat

4) - Adicione a seguinte configuração à sua settings.py:

    INSTALLED_APPS = [
        # ...
        'chat',
    ]

5) Crie um serializer para a sua API:

    # chat/serializers.py
    from rest_framework import serializers
    
    class ChatSerializer(serializers.Serializer):
        message = serializers.CharField()

6) Crie uma view para o seu serializer:

    # chat/views.py
    from rest_framework import views
    from rest_framework.response import Response
    from .serializers import ChatSerializer
    
    class ChatView(views.APIView):
        serializer_class = ChatSerializer
    
        def post(self, request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
    
            message = serializer.validated_data['message']
    
            # Aqui você pode inserir o código de previsão do ChatGPT
            response = {'message': message}
    
            return Response(response)

7) Adicione uma URL para sua view:

    # chatgpt_api/urls.py
    from django.urls import path
    from chat.views import ChatView
    
    urlpatterns = [
        # ...
        path('chat/', ChatView.as_view(), name='chat'),
    ]

8) Execute o servidor de desenvolvimento:
 - python manage.py runserver

9) - Agora você pode testar sua API enviando uma requisição POST para o endereço http://localhost:8000/chat/ com um objeto JSON no corpo da requisição, como este:

    {
        "message": "Olá, como posso ajudá-lo hoje?"
    }

 - Este é um exemplo simples para mostrar como você pode criar uma API de consumo para o ChatGPT em Django-Python. Você precisará adicionar o código de previsão do ChatGPT para funcionar corretamente.

