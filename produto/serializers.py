from rest_framework import serializers, generics
from produto.models import Produto, EstoqueProduto


class EstoqueProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueProduto
        fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    quantidade = serializers.ReadOnlyField(source='estoque_produto.quantidade')

    class Meta:
        model = Produto
        fields = "__all__"

    @staticmethod
    def validate(data):
        nome = data.get('nome', None)

        if not nome:
            raise serializers.ValidationError(
                {"nome": "Campo obrigatóŕio faltando."}
            )
        elif Produto.objects.filter(nome=nome).exists():
            raise serializers.ValidationError(
                {"nome": "O nome do produto já está cadastrado"}
            )
        return data




