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


class RepoClienteEscritaTeste:

    @staticmethod
    def criar_cliente(
        nome: str,
        cpf: str,
        telefone_1: str,
        email: str,
    ) -> Cliente:
        cliente = Cliente.objects.create(
            nome=nome,
            cpf=cpf,
            telefone_1=telefone_1,
            email=email,
        )
        return cliente

    @staticmethod
    def deletar_todos_os_clientes():
        Cliente.objects.all().delete()


class RepoClienteLeituraTeste:

    @staticmethod
    def consultar_unico_objeto_existente():
        cliente = Cliente.objects.get()
        return cliente

    @staticmethod
    def contar_todos_os_clientes():
        quantidade_de_clientes = Cliente.objects.count()
        return quantidade_de_clientes
