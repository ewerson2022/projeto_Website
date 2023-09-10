from django.test import RequestFactory, TestCase
from django.contrib import messages
from django.shortcuts import redirect
from cadastro.views import cadastro
import unittest
from django.test.client import  Client
from django.contrib.messages.storage.fallback import FallbackStorage
from django.urls import reverse
import unittest
from django.test import Client


"""class CadastroViewTestCase(TestCase):

    def test_post_com_nome_vazio(self):
        data = {
            'email': 'teste@email.com',
            'password': '123456',
        }
        response = self.client.post('/cadastro/', data)
        self.assertEqual(response.status_code, 404)
        """
        


class CadastroViewTestCase(TestCase):
    def test_post_com_nome_vazio(self):
        data = {
            'nome': '',
            'email': 'teste@example.com',
            'password': '123456',
        }
        response = self.client.post('/cadastro/', data)
        self.assertRedirects(response, '/cadastro/')
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'O campo nome não pode ficar vazio')






if __name__ == '__main__':
    unittest.main()
