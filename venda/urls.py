from django.urls import include, path
from rest_framework import routers

from venda.views import VendasViewSet

router = routers.DefaultRouter()
router.register("vendas", VendasViewSet, basename="Vendas")

urlpatterns = [
    path("", include(router.urls)),
]
