from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.forms import *
from django.db import models
from django import forms



class Estabelecimento(models.Model):
    
        user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
        numero_estabelecimento = models.CharField(max_length=20)
        razao_social = models.CharField(max_length=100)
        cnpj = models.CharField(max_length=20, unique=True)
        endereco = models.CharField(max_length=200)

def __str__(self):
    return self.razao_social

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        exclude = ['user']
        fields = '__all__'
    
    
class Loja(models.Model):
    numero_loja = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    
def __str__(self):
    return self.razao_social
    
    
class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        exclude = ['estabelecimento']
        fields = '__all__'
    



    


