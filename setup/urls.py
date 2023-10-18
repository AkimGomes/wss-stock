from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login", TokenObtainPairView.as_view()),
    path("login/refresh", TokenRefreshView.as_view()),
    path('', include("produto.urls")),
    path('', include("venda.urls")),
    path('', include("orcamento.urls")),
    path('', include("cliente.urls"))
]
