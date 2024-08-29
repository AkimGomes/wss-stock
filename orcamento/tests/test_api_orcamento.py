from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from orcamento.models import Orcamento
from cliente.models import Cliente
from rest_framework import status

from orcamento.repo.orcamento import (
    RepoOrcamentoEscritaTeste,
    RepoOrcamentoLeituraTeste,
)


class OrcamentoTestCase(APITestCase):

    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(
            username="usuario_test", password="senha_test"
        )

        token = self.obter_token()  # Obter token de autenticação
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + token
        )  # Configurar as credenciais para usar o token

        # Criando os dados necessários para os testes de Orçamento
        self.list_url = reverse("Orcamento-list")
        self.cliente = Cliente.objects.create(
            nome="Cliente de Teste",
            cpf="12345678900",
            telefone_1="11912345678",
            email="teste@teste.com",
        )
        self.orcamento = RepoOrcamentoEscritaTeste.criar_orcamento(
            nome="Orçamento de Teste",
            descricao="Orçamento usado para realização de testes da API",
            cliente_orcamento=self.cliente,
            observacao="Produto requer manutenção",
            valor_orcamento=200.0,
        )

        self.url_de_orcamento_detalhada = reverse(
            "Orcamento-detail", args=[self.orcamento.id]
        )

    def obter_token(self):
        """
        Obtém um token de acesso JWT para o usuário de teste
        """
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "usuario_test", "password": "senha_test"},
        )
        return response.data["access"]

    def test_requisicao_get_para_listar_orcamentos(self):
        """
        Teste para verificar se a requisição GET está listando os orçamentos
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_orcamento(self):
        """
        Teste para verificar se a requisição POST está criando um orçamento
        """
        RepoOrcamentoEscritaTeste.deletar_todos_os_orcamentos()  # Limpa os dados de Orçamento para garantir consistência

        data = {
            "nome": "Orçamento de Teste",
            "descricao": "Descrição do orçamento de teste.",
            "observacao": "Observação sobre o orçamento.",
            "cliente_orcamento": {
                "nome": "Cliente de Teste",
                "cpf": "12345678900",
                "telefone_1": "11912345678",
                "email": "cliente@teste.com",
            },
            "valor_orcamento": 300.0,
        }
        response = self.client.post(self.list_url, data=data, format="json")

        orcamento = RepoOrcamentoLeituraTeste.consultar_orcamento_pelo_nome(
            nome="Orçamento de Teste"
        )
        quantidade_de_orcamentos = (
            RepoOrcamentoLeituraTeste.contar_todos_os_orcamentos()
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(quantidade_de_orcamentos, 1)
        self.assertEqual(orcamento.nome, "Orçamento de Teste")

    def test_requisicao_delete_para_deletar_orcamento(self):
        """
        Teste para verificar a requisição DELETE permitida para deletar um orçamento
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.url_de_orcamento_detalhada)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(self.url_de_orcamento_detalhada)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_requisicao_put_para_atualizar_orcamento(self):
        """
        Teste para verificar a requisição PUT para atualizar um orçamento
        """
        data = {
            "nome": "Orçamento de Teste ATUALIZADO",
            "descricao": "Orçamento de Teste usado para realização de testes da API, atualização de Orçamento",
            "observacao": "Orçamento requer manutenção geral, teste PUT",
            "valor_orcamento": 1000.0,
        }

        response = self.client.put(self.url_de_orcamento_detalhada, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        orcamento_atualizado = (
            RepoOrcamentoLeituraTeste.consultar_unico_objeto_existente()
        )

        self.assertEqual(orcamento_atualizado.nome, "Orçamento de Teste ATUALIZADO")
        self.assertEqual(
            orcamento_atualizado.descricao,
            "Orçamento de Teste usado para realização de testes da API, atualização de Orçamento",
        )
        self.assertEqual(
            orcamento_atualizado.observacao,
            "Orçamento requer manutenção geral, teste PUT",
        )
        self.assertEqual(orcamento_atualizado.valor_orcamento, 1000.0)
