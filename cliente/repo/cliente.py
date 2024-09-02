from django.db.models import QuerySet

from cliente.models import Cliente


class RepoClienteLeitura:

    @staticmethod
    def consultar_clientes_ordenados_pela_data_de_cadastro():
        clientes = Cliente.objects.all().order_by("data_cadastro")
        return clientes

    @staticmethod
    def consultar_cliente_pelo_nome(nome: str) -> QuerySet[Cliente]:
        cliente = Cliente.objects.filter(nome__icontains=nome)
        return cliente
