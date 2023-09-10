from django.db import models
from django import forms

class Login_usuario(models.Model):
    
    email = models.EmailField(max_length=30)
    senha = models.CharField(max_length=12)

    
class Cadastro_usuario(models.Model):
     email = models.EmailField(max_length=30,unique=True)
     senha = models.CharField(max_length=12)
     
class CadastroForm(forms.Form):
    id = models.IntegerField(primary_key=True)
    username = forms.CharField(label='Nome de usuário', max_length=150)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    


    
    
    
