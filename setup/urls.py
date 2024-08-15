from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

schema_view = get_schema_view(
   openapi.Info(
      title="WSS-Stock",
      default_version='v1',
      description="Sistema de gerenciamento de estoque para pequenas empresas",
      terms_of_service="#",
      contact=openapi.Contact(email="wss-stock@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path('', include("produto.urls")),
    path('', include("venda.urls")),
    path('', include("orcamento.urls")),
    path('', include("cliente.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
