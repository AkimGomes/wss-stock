from django.db.models import QuerySet

from orcamento.models import Orcamento
from orcamento.serializers import OrcamentoSerializer


class RepoOrcamentoLeitura:

    @staticmethod
    def consultar_orcamentos_ativos() -> QuerySet[Orcamento]:
        orcamentos = Orcamento.objects.filter(ativo_inativo=True).order_by(
            "data_orcamento"
        )
        return orcamentos

    @staticmethod
    def consultar_orcamento_pelo_nome(nome: str) -> QuerySet[Orcamento]:
        orcamento = Orcamento.objects.filter(nome__icontains=nome)
        return orcamento


class RepoOrcamentoEscrita:

    @staticmethod
    def salvar_serializer(orcamento_serializer: OrcamentoSerializer):
        return orcamento_serializer.save()

    @staticmethod
    def salvar(orcamento: Orcamento):
        orcamento.save()

    @staticmethod
    def deletar(orcamento: Orcamento):
        orcamento.delete()


class RepoOrcamentoLeituraTeste:

    @staticmethod
    def consultar_unico_objeto_existente():
        orcamento = Orcamento.objects.get()
        return orcamento

    @staticmethod
    def consultar_orcamento_pelo_nome(nome: str) -> QuerySet[Orcamento]:
        orcamento = Orcamento.objects.filter(nome__icontains=nome).first()
        return orcamento

    @staticmethod
    def contar_todos_os_orcamentos():
        quantidade_de_orcamentos = Orcamento.objects.count()
        return quantidade_de_orcamentos


class RepoOrcamentoEscritaTeste:

    @staticmethod
    def criar_orcamento(
        nome: str,
        descricao: str,
        cliente_orcamento: str,
        observacao: str,
        valor_orcamento: str,
    ) -> Orcamento:
        orcamento = Orcamento.objects.create(
            nome=nome,
            descricao=descricao,
            cliente_orcamento=cliente_orcamento,
            observacao=observacao,
            valor_orcamento=valor_orcamento,
        )
        return orcamento

    @staticmethod
    def deletar_todos_os_orcamentos():
        Orcamento.objects.all().delete()
