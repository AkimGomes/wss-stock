from rest_framework import serializers

from venda.models import ProdutoVenda, Venda


class ProdutoVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoVenda
        fields = "__all__"


class VendaSerializer(serializers.ModelSerializer):
    produtos_venda = ProdutoVendaSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = "__all__"
