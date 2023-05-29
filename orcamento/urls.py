from django.urls import path
from .views import visualizar_orcamentos, cadastrar_orcamento_cliente

urlpatterns = [
    path('visualizar_orcamentos', visualizar_orcamentos, name='visualizar_orcamentos'),
    path('cadastrar_orcamento_cliente', cadastrar_orcamento_cliente, name='cadastrar_orcamento_cliente'),
]
