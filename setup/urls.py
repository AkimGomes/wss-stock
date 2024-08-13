from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path('', include("produto.urls")),
    path('', include("venda.urls")),
    path('', include("orcamento.urls")),
    path('', include("cliente.urls"))
]
