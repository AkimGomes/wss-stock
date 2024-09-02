from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cliente.models import Cliente
from cliente.repo.cliente import RepoClienteLeitura
from cliente.serializers import ClienteSerializer
from cliente.services.cliente import ClienteService

cliente_service = ClienteService()


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API de Clientes
    """

    permission_classes = (IsAuthenticated,)
    queryset = RepoClienteLeitura.consultar_clientes_ordenados_pela_data_de_cadastro()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["nome"]
    search_fields = ["nome", "cpf"]
    serializer_class = ClienteSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def buscar(self, request):
        nome = self.request.query_params.get("buscar", None)

        if nome:
            clientes = cliente_service.consultar_cliente_especifico_pelo_nome(nome=nome)

        serializer = self.get_serializer(clientes, many=True)
        return Response(serializer.data)
