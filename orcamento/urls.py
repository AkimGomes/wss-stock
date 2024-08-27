from django.urls import path, include
from rest_framework import routers

from orcamento.views import OrcamentoViewSet

router = routers.DefaultRouter()
router.register("orcamento", OrcamentoViewSet, basename="Orcamento")

urlpatterns = [path("", include(router.urls))]
