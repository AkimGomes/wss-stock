from django.urls import path, include
from rest_framework import routers
from produto.views import ProdutosViewSet, EstoqueProdutoViewSet

# from produto.views import index, cadastro_produto, atualizar_produto, deletar_produto, buscar, ProdutosViewSet

# urlpatterns = [
#     path("", index, name="index"),
#     path("cadastro_produto", cadastro_produto, name="cadastro_produto"),
#     path("buscar", buscar, name="buscar"),
#     path("deletar_produto/<int:id>", deletar_produto, name="deletar_produto"),
#     path("atualizar_produto/<int:id>", atualizar_produto, name="atualizar_produto"),
# ]

router = routers.DefaultRouter()
router.register("produtos", ProdutosViewSet, basename="Produtos")
router.register("estoque_produtos", EstoqueProdutoViewSet, basename="EstoqueProdutos")

urlpatterns = [
    path("", include(router.urls)),
]
