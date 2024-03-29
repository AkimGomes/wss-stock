from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cliente.serializers import ClienteSerializer
from orcamento.models import Orcamento
from orcamento.serializers import OrcamentoSerializer


class OrcamentoViewSet(viewsets.ModelViewSet):
    """
    API de Orçamento
    """
    permission_classes = (IsAuthenticated,)
    queryset = Orcamento.objects.filter(ativo_inativo=True).order_by('data_orcamento')
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["data_orcamento"]
    search_fields = ["nome", "cliente_orcamento"]
    serializer_class = OrcamentoSerializer

    def create(self, request, *args, **kwargs):
        orcamento_data = request.data

        # Primeiro, crie o orçamento sem um cliente associado
        orcamento_serializer = OrcamentoSerializer(data=orcamento_data)
        if orcamento_serializer.is_valid():
            orcamento_instance = orcamento_serializer.save()
        else:
            return Response(orcamento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Em seguida, crie o cliente associado ao orçamento
        cliente_data = orcamento_data.get('cliente_orcamento')
        if cliente_data:
            cliente_serializer = ClienteSerializer(data=cliente_data)
            if cliente_serializer.is_valid():
                cliente_instance = cliente_serializer.save()
                orcamento_instance.cliente_orcamento = cliente_instance
                orcamento_instance.save()
            else:
                # Se houver erros de validação, você pode excluir o orçamento recém-criado
                orcamento_instance.delete()
                return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(orcamento_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Primeiro, serialize o objeto existente para verificar as mudanças
        existing_data = OrcamentoSerializer(instance).data

        # Em seguida, serialize os dados da solicitação
        serializer = OrcamentoSerializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()

            # Compare os dados antes e depois da atualização
            updated_data = serializer.data
            if existing_data != updated_data:
                return Response(updated_data, status=status.HTTP_200_OK)

            return Response({"message": "Nenhum dado foi alterado."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def buscar(self, request):
        nome = self.request.query_params.get('buscar', None)
        orcamentos = Orcamento.objects.all()

        if nome:
            orcamentos = orcamentos.filter(nome__icontains=nome)

            if not orcamentos.exists():
                return Response({"message": "Nenhum orçamento encontrado!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(orcamentos, many=True)
        return Response(serializer.data)
