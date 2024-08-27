from django.contrib import admin
from cliente.models import Cliente


class ListandoClientes(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "cpf",
        "telefone_1",
        "telefone_2",
        "email",
        "data_cadastro",
        "ativo_inativo",
    )
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_editable = ("ativo_inativo",)
    list_per_page = 10


admin.site.register(Cliente, ListandoClientes)
