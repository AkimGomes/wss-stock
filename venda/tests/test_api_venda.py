from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from produto.models import Produto
from venda.models import Venda, ProdutoVenda
from rest_framework import status


class VendaTestCase(APITestCase):

    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(
            username="usuario_test", password="senha_test"
        )

        token = self.obter_token()  # Obter token de autenticação
        self.client.credentials(
            HTTP_AUTHORIZATION="Bearer " + token
        )  # Configurar as credenciais para usar o token

        # Criando os dados necessários para os testes de Produto
        self.list_url = reverse("Vendas-list")
        self.produto = Produto.objects.create(
            nome="Produto de Teste",
            descricao="Produto usado para realização de testes da API",
            preco_custo=10.0,
            preco_venda=15.0,
            tipo_produto="Produto de mostruário",
            descricao_tipo="Produtos de mostruário são usados apenas de exemplo",
        )
        self.produto_venda = ProdutoVenda.objects.create(
            produto_vendido=self.produto,
            quantidade=10,
        )
        self.venda = Venda.objects.create(
            observacao="Venda do Cliente Josias",
            preco_total=12.00,
        )
        self.venda.produtos_venda.add(self.produto_venda)
        self.url_de_venda_detalhada = reverse("Vendas-detail", args=[self.venda.id])

    def obter_token(self):
        """
        Obtém um token de acesso JWT para o usuário de teste
        """
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "usuario_test", "password": "senha_test"},
        )
        return response.data["access"]

    def test_requisicao_get_para_listar_vendas(self):
        """
        Teste para verificar se a requisição GET está listando as vendas
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_venda(self):
        """
        Teste para verificar se a requisição POST está criando uma venda
        """
        Venda.objects.all().delete()  # Limpa os dados de Venda para garantir consistência

        data = {
            "observacao": "Venda do Cliente Josias teste de POST",
            "preco_total": 24.00,
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Venda.objects.count(), 1)
        self.assertEqual(
            Venda.objects.get().observacao, "Venda do Cliente Josias teste de POST"
        )

    def test_requisicao_delete_para_deletar_venda(self):
        """
        Teste para verificar a requisição DELETE permitida para deletar uma venda
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.url_de_venda_detalhada)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(self.url_de_venda_detalhada)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_requisicao_put_para_atualizar_venda(self):
        """
        Teste para verificar a requisição PUT para atualizar uma venda
        """
        data = {
            "observacao": "Venda do Cliente Josias teste de ATUALIZAÇÃO",
            "preco_total": 48.00,
        }

        response = self.client.put(self.url_de_venda_detalhada, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        venda_atualizada = Venda.objects.get()

        self.assertEqual(
            venda_atualizada.observacao, "Venda do Cliente Josias teste de ATUALIZAÇÃO"
        )
        self.assertEqual(venda_atualizada.preco_total, 48.00)
