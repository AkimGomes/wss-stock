from django.urls import path
from produto.views import index, cadastro_produto, atualizar_produto, deletar_produto, buscar

urlpatterns = [
    path("", index, name="index"),
    path("cadastro_produto", cadastro_produto, name="cadastro_produto"),
    path("buscar", buscar, name="buscar"),
    path("deletar_produto/<int:id>", deletar_produto, name="deletar_produto"),
    path("atualizar_produto/<int:id>", atualizar_produto, name="atualizar_produto"),
]
