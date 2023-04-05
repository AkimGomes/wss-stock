from django.urls import path
from produto.views import index, cadastro_produto

urlpatterns = [
    path("", index, name="index"),
    path("cadastro_produto", cadastro_produto, name="cadastro_produto"),
]
