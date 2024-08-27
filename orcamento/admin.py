from django.contrib import admin
from orcamento.models import Orcamento


class ListandoOrcamentos(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "descricao",
        "valor_orcamento",
        "cliente_orcamento",
        "data_orcamento",
        "ativo_inativo",
    )
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_editable = ("ativo_inativo",)
    list_per_page = 10


admin.site.register(Orcamento, ListandoOrcamentos)
