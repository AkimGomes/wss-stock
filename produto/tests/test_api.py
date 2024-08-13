from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from django.urls import reverse
from produto.models import Produto, EstoqueProduto
from rest_framework import status


class ProdutoTestCase(APITestCase):

    def setUp(self):
        # Criar um usuário de teste
        self.user = User.objects.create_user(username='usuario_test', password='senha_test')

        token = self.obter_token()  # Obter token de autenticação
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token) # Configurar as credenciais para usar o token

        # Criando os dados necessários para os testes de Produto
        self.list_url = reverse('Produtos-list')
        self.produto = Produto.objects.create(
            nome="Produto de Teste",
            descricao="Produto usado para realização de testes da API",
            preco_custo=10.0,
            preco_venda=15.0,
            tipo_produto="Produto de mostruário",
            descricao_tipo="Produtos de mostruário são usados apenas de exemplo",
        )
        self.url_de_produto_detalhada = reverse('Produtos-detail', args=[self.produto.id])
        self.estoque_produto = EstoqueProduto.objects.create(
            produto=self.produto,
            quantidade=10,
        )

    def obter_token(self):
        """
        Obtém um token de acesso JWT para o usuário de teste
        """
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'usuario_test',
            'password': 'senha_test'
        })
        return response.data['access']

    def test_requisicao_get_para_listar_produtos(self):
        """
        Teste para verificar se a requisição GET está listando os produtos
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_produto(self):
        """
        Teste para verificar se a requisição POST está criando um produto
        """
        Produto.objects.all().delete() # Limpa os dados de Produtos para garantir consistência
        EstoqueProduto.objects.all().delete() # Limpa os dados de EstoqueProduto para garantir consistência

        data = {
            "nome": "Produto de Teste para POST",
            "descricao": "Produto usado para realização de testes da API",
            "preco_custo": 10.0,
            "preco_venda": 15.0,
            "tipo_produto": "Produto de mostruário",
            "descricao_tipo": "Produtos de mostruário são usados apenas de exemplo",
            "quantidade": 10,
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(Produto.objects.get().nome, 'Produto de Teste para POST')

    def test_requisicao_delete_para_deletar_produto(self):
        """
        Teste para verificar a requisição DELETE permitida para deletar um produto
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(self.url_de_produto_detalhada)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(self.url_de_produto_detalhada)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_requisicao_put_para_atualizar_produto(self):
        """
        Teste para verificar a requisição PUT para atualizar um produto
        """
        data = {
            "nome": "Produto de Teste ATUALIZADO",
            "descricao": "Produto usado para realização de testes da API, atualização de Produto",
            "preco_custo": 10.0,
            "preco_venda": 15.0,
            "tipo_produto": "Produto de mostruário",
            "descricao_tipo": "Produtos de mostruário são usados apenas de exemplo",
            "quantidade": 100,
        }

        response = self.client.put(self.url_de_produto_detalhada, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

