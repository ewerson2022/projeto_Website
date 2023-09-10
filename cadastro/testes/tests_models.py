from django.test import TestCase
import unittest
from cadastro.models import Login_usuario, Cadastro_usuario, CadastroForm


class ModelTest(unittest.TestCase):
    def test_login_usuario(self):
        login = Login_usuario(email='teste@example.com', senha='senha123')
        self.assertEqual(login.email, 'teste@example.com')
        self.assertEqual(login.senha, 'senha123')

    def test_cadastro_usuario(self):
        cadastro = Cadastro_usuario(email='teste@example.com', senha='senha123')
        self.assertEqual(cadastro.email, 'teste@example.com')
        self.assertEqual(cadastro.senha, 'senha123')

class FormTest(unittest.TestCase):
    def test_cadastro_form(self):
        form_data = {
            'username': 'usuarioteste',
            'email': 'teste@example.com',
            'password': 'senha123',
        }
        form = CadastroForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['username'], 'usuarioteste')
        self.assertEqual(form.cleaned_data['email'], 'teste@example.com')
        self.assertEqual(form.cleaned_data['password'], 'senha123')

if __name__ == '__main__':
    unittest.main()
