from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cliente.models import Cliente
from cliente.serializers import ClienteSerializer
from orcamento.models import Orcamento
from orcamento.serializers import OrcamentoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    API de Clientes
    """
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer

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
