from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("produto.urls")),
    path('', include("venda.urls")),
    path('', include("orcamento.urls")),
]
