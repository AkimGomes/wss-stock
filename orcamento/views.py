from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from orcamento.repo.orcamento import RepoOrcamentoLeitura
from orcamento.serializers import OrcamentoSerializer
from orcamento.services.orcamento import OrcamentoService

orcamento_service = OrcamentoService()


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
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def buscar(self, request):
        nome = self.request.query_params.get("buscar", None)

        if nome:
            orcamentos = orcamento_service.consultar_orcamento_especifico_pelo_nome(
                nome=nome
            )

        serializer = self.get_serializer(orcamentos, many=True)
        return Response(serializer.data)
