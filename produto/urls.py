from django.urls import path, include
from rest_framework import routers
from produto.views import ProdutosViewSet, EstoqueProdutoViewSet


router = routers.DefaultRouter()
router.register("produtos", ProdutosViewSet, basename="Produtos")
router.register("estoque_produtos", EstoqueProdutoViewSet, basename="EstoqueProdutos")

urlpatterns = [
    path("", include(router.urls)),
]
