from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from produto.models import EstoqueProduto, Produto
from venda.models import Venda, ProdutoVenda
from venda.serializers import VendaSerializer


class VendasViewSet(viewsets.ModelViewSet):
    """
    API de ProdutoVenda
    """

    permission_classes = (IsAuthenticated,)
    queryset = Venda.objects.all().order_by('id')
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["data"]
    search_fields = ["data", "preco_total"]
    serializer_class = VendaSerializer

    def create(self, request, *args, **kwargs):
        venda_serializer = self.get_serializer(data=request.data)
        venda_serializer.is_valid(raise_exception=True)
        venda = venda_serializer.save()

        total_preco = 0

        produto_vendas = request.data.get('produtos_venda', [])
        venda.produtos_venda.clear()
        estoque_insuficiente = False  # Variável para rastrear se há estoque insuficiente

        for produto_data in produto_vendas:
            produto_id = produto_data.get('produto_vendido')
            quantidade = produto_data.get('quantidade')

            if produto_id and quantidade >= 0:
                produto = Produto.objects.get(pk=produto_id)
                estoque_produto = EstoqueProduto.objects.get(produto=produto_id)

                if quantidade <= estoque_produto.quantidade:
                    produto_venda = ProdutoVenda.objects.create(
                        produto_vendido=produto,
                        quantidade=quantidade
                    )
                    venda.produtos_venda.add(produto_venda)

                    total_preco += produto_venda.preco

                    estoque_produto.quantidade -= quantidade
                    estoque_produto.save()
                else:
                    estoque_insuficiente = True  # Marque como estoque insuficiente

        if estoque_insuficiente:
            venda.delete()  # Exclui a venda se houver estoque insuficiente
            return Response({'detail': 'Não é possível, produto com baixo estoque.'}, status=status.HTTP_400_BAD_REQUEST)

        venda.preco_total = total_preco
        venda.save()

        headers = self.get_success_headers(venda_serializer.data)
        return Response(venda_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def venda_info(self, request, pk=None):
        venda = self.get_object()

        venda_serializer = VendaSerializer(venda)

        data = {
            'venda': venda_serializer.data,
        }
        return Response(data, status=200)

