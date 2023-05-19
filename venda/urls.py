from django.urls import path
from .views import criar_venda

urlpatterns = [
    path('criar_venda', criar_venda, name='criar_venda'),
]
