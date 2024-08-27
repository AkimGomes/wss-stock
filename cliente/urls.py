from django.urls import path, include
from rest_framework import routers

from cliente.views import ClienteViewSet

router = routers.DefaultRouter()
router.register("cliente", ClienteViewSet, basename="Cliente")

urlpatterns = [path("", include(router.urls))]
