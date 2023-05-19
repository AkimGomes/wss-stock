from django.urls import path
from .views import criar_venda, visualizar_vendas, excluir_venda

urlpatterns = [
    path('criar_venda', criar_venda, name='criar_venda'),
    path('visualizar_vendas/', visualizar_vendas, name='visualizar_vendas'),
    path('venda/excluir/<int:venda_id>/', excluir_venda, name='excluir_venda'),
]
