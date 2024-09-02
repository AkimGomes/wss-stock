from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from cliente.models import Cliente
from rest_framework import status

from cliente.repo.cliente import RepoClienteEscritaTeste, RepoClienteLeituraTeste


class ClienteTestCase(APITestCase):

    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(
            username="usuario_test", password="senha_test"
        )

        token = self.obter_token()  # Obter token de autenticação
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + token
        )  # Configurar as credenciais para usar o token

        # Criando os dados necessários para os testes de Cliente
        self.list_url = reverse("Cliente-list")
        self.cliente = RepoClienteEscritaTeste.criar_cliente(
            nome="Cliente de Teste",
            cpf="12345678900",
            telefone_1="11912345678",
            email="teste@teste.com",
        )
        self.url_de_cliente_detalhada = reverse(
            "Cliente-detail", args=[self.cliente.id]
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

    def test_requisicao_get_para_listar_clientes(self):
        """
        Teste para verificar se a requisição GET está listando os clientes
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_cliente(self):
        """
        Teste para verificar se a requisição POST está criando um cliente
        """
        RepoClienteEscritaTeste.deletar_todos_os_clientes()  # Limpa os dados de Clientes para garantir consistência

        data = {
            "nome": "Cliente de Teste para POST",
            "cpf": "00000000023",
            "telefone_1": "13988883333",
            "email": "teste@teste.com",
        }
        response = self.client.post(self.list_url, data=data)

        cliente = RepoClienteLeituraTeste.consultar_unico_objeto_existente()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RepoClienteLeituraTeste.contar_todos_os_clientes(), 1)
        self.assertEqual(cliente.nome, "Cliente de Teste para POST")

    def test_requisicao_delete_para_deletar_cliente(self):
        """
        Teste para verificar a requisição DELETE permitida para deletar um cliente
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.url_de_cliente_detalhada)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(self.url_de_cliente_detalhada)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_requisicao_put_para_atualizar_cliente(self):
        """
        Teste para verificar a requisição PUT para atualizar um cliente
        """
        data = {
            "nome": "Cliente de Teste ATUALIZADO",
            "cpf": "00000000011",
            "telefone_1": "13988883333",
            "email": "teste_att@teste.com",
        }

        response = self.client.put(self.url_de_cliente_detalhada, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        cliente_atualizado = RepoClienteLeituraTeste.consultar_unico_objeto_existente()

        self.assertEqual(cliente_atualizado.nome, "Cliente de Teste ATUALIZADO")
        self.assertEqual(cliente_atualizado.cpf, "00000000011")
