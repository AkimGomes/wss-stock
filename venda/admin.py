from django.contrib import admin
from venda.models import ProdutoVenda, Venda


class ListandoVendas(admin.ModelAdmin):
    list_display = ("id", "observacao", "data", "preco_total")
    list_display_links = ("data",)
    search_fields = ("id", "data")
    list_per_page = 10


admin.site.register(Venda, ListandoVendas)


class ListandoProdutoVenda(admin.ModelAdmin):
    list_display = ("produto_vendido", "quantidade", "preco")
    list_display_links = ("produto_vendido",)
    search_fields = ("produto_vendido",)
    list_per_page = 10


admin.site.register(ProdutoVenda, ListandoProdutoVenda)
