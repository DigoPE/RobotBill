from django.urls import path, include
from rest_framework import routers
#from rest_framework.authtoken import views

from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
#from rest_framework import permissions

from .views import PortasViewSet, PlacasViewSet
#import ApiSystem.views

#Colocar no router apenas as API's vindas do Banco de Dados.
#API's de controle do Arduino, colocar na urls do "siteconfig"
router = routers.DefaultRouter()
router.register('apiPortas', PortasViewSet)
router.register('apiPlacas', PlacasViewSet)


#Schema View para o Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Robo Bill API",
        default_version='v1',
        description="Visualizações das API's.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rodrigo.barros1981@hotmail.com"),
        license=openapi.License(name="Free License"),
    ),
    public=True,
    #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('ApiSystem/', include(router.urls)),
    #path('apiBOApp-auth/', include('rest_framework.urls')),
    #path('apiBOApp-auth/', views.obtain_auth_token), #API de auteticação que gero o Token para poder consumir o 'apiBOApp/'
]

# URL do Swagger
urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # noqa E501
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa E501
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa E501
]