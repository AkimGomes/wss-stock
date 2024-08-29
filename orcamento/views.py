from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cliente.services.cliente import ClienteService
from orcamento.repo.orcamento import RepoOrcamentoLeitura
from orcamento.serializers import OrcamentoSerializer
from orcamento.services.orcamento import OrcamentoService

orcamento_service = OrcamentoService()
cliente_service = ClienteService()


class OrcamentoViewSet(viewsets.ModelViewSet):
    """
    API de Orçamento
    """

    permission_classes = (IsAuthenticated,)
    queryset = RepoOrcamentoLeitura.consultar_orcamentos_ativos()
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

        if orcamento_data.get("cliente_orcamento"):
            orcamento_serializer = OrcamentoSerializer(data=orcamento_data)
            orcamento_service.criar_orcamento(orcamento_serializer=orcamento_serializer)

        return Response(orcamento_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
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

            return Response(
                {"message": "Nenhum dado foi alterado."}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def buscar(self, request):
        nome = self.request.query_params.get("buscar", None)

        if nome:
            orcamentos = RepoOrcamentoLeitura.consultar_orcamento_pelo_nome(nome=nome)

            if not orcamentos.exists():
                return Response(
                    {"message": "Nenhum orçamento encontrado!"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        serializer = self.get_serializer(orcamentos, many=True)
        return Response(serializer.data)
