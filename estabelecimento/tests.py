from django.test import TestCase
import unittest
import unittest
from django.contrib.auth import get_user_model
from estabelecimento.models import Estabelecimento, Loja
from estabelecimento.models import EstabelecimentoForm, LojaForm

User = get_user_model()

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_estabelecimento(self):
        estabelecimento = Estabelecimento.objects.create(
            user=self.user,
            numero_estabelecimento='123',
            razao_social='Razão Social',
            cnpj='1234567890',
            endereco='Endereço'
        )
        self.assertEqual(estabelecimento.numero_estabelecimento, '123')
        self.assertEqual(estabelecimento.razao_social, 'Razão Social')
        self.assertEqual(estabelecimento.cnpj, '1234567890')
        self.assertEqual(estabelecimento.endereco, 'Endereço')

    def test_loja(self):
        estabelecimento = Estabelecimento.objects.create(
            user=self.user,
            numero_estabelecimento='123',
            razao_social='Razão Social',
            cnpj='1234567890',
            endereco='Endereço'
        )
        loja = Loja.objects.create(
            numero_loja='456',
            razao_social='Razão Social Loja',
            endereco='Endereço Loja',
            estabelecimento=estabelecimento
        )
        self.assertEqual(loja.numero_loja, '456')
        self.assertEqual(loja.razao_social, 'Razão Social Loja')
        self.assertEqual(loja.endereco, 'Endereço Loja')
        self.assertEqual(loja.estabelecimento, estabelecimento)

class FormTest(unittest.TestCase):
    def test_estabelecimento_form(self):
        form_data = {
            'numero_estabelecimento': '123',
            'razao_social': 'Razão Social',
            'cnpj': '1234567890',
            'endereco': 'Endereço'
        }
        form = EstabelecimentoForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['numero_estabelecimento'], '123')
        self.assertEqual(form.cleaned_data['razao_social'], 'Razão Social')
        self.assertEqual(form.cleaned_data['cnpj'], '1234567890')
        self.assertEqual(form.cleaned_data['endereco'], 'Endereço')

    def test_loja_form(self):
        estabelecimento = Estabelecimento.objects.create(
            user=User.objects.create_user(username='testuser', password='testpassword'),
            numero_estabelecimento='123',
            razao_social='Razão Social',
            cnpj='1234567890',
            endereco='Endereço'
        )
        form_data = {
            'numero_loja': '456',
            'razao_social': 'Razão Social Loja',
            'endereco': 'Endereço Loja',
            'estabelecimento': estabelecimento.pk
        }
        form = LojaForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['numero_loja'], '456')
        self.assertEqual(form.cleaned_data['razao_social'], 'Razão Social Loja')
        self.assertEqual(form.cleaned_data['endereco'], 'Endereço Loja')
        self.assertEqual(form.cleaned_data['estabelecimento'], estabelecimento)

if __name__ == '__main__':
    unittest.main()
