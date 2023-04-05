from django.contrib import admin

from produto.models import Produto


class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco_custo", "preco_venda", "tipo_produto", "publicado")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("nome", "tipo_produto")
    list_editable = ("publicado", )
    list_per_page = 10


admin.site.register(Produto, ListandoProdutos)
