from rest_framework import serializers

from cliente.serializers import ClienteSerializer
from orcamento.models import Orcamento


class OrcamentoSerializer(serializers.ModelSerializer):
    cliente_orcamento = ClienteSerializer(read_only=True)

    class Meta:
        model = Orcamento
        fields = "__all__"

