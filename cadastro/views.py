from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import login as login_django, logout as logout_django
from django.contrib import messages, auth
from django.contrib.messages import constants
from estabelecimento.views import listar_estabelecimento, novo_estabelecimento
from estabelecimento.models import Estabelecimento

    
    

def cadastro(request): 
    
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        if  not nome.strip():
         #   messages.error(request,'o campo nome não pode ficar vazio')
            return redirect('cadastro')
        
        if not email.strip():
            messages.error(request,'o campo email não pode ficar vazio')
            return redirect('cadastro')
        
        if len(senha) < 8:
       #     messages.error(request,'sua senha deve ter no minimo 8 caracteres')
            return redirect('cadastro')
        
        
        if User.objects.filter(email=email).exists():
      #      messages.add_message(request, constants.WARNING, 'Já existe um usuario com esse Email')
            return redirect('cadastro')
        
        if User.objects.filter(username=nome).exists():
      #      messages.add_message(request, constants.WARNING, 'Já existe um usuario com esse nome')
            return redirect('cadastro')
        
        try:
     
            usuario =  User.objects.create_user(username = nome, email=email, password = senha)
            usuario.save()
       #     messages.add_message(request, constants.SUCCESS, 'CADASTRO REALIZADO COM SUCESSO')
            return redirect('login')
            
        except:    
         #   messages.add_message(request, constants.ERROR, 'ERRO NO SISTEMA')
            return redirect('cadastro')
    else:
        return render(request,'cadastro.html')
  
def login(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        login_usuario = auth.authenticate(username = username,
                                          password = password)
        
        if not login_usuario:
       #     messages.add_message(request,constants.WARNING,'usuario ou senha invalidos !')
            return render(request, 'login.html')
        
        else:
        #        messages.add_message(request,constants.WARNING,'você foi logado com sucesso!')
                login_django(request,login_usuario)
                
               # Verifique se o usuário possui um estabelecimento associado
                if Estabelecimento.objects.filter(user=request.user).exists():
                    return redirect(listar_estabelecimento)  # Redireciona para a lista de estabelecimentos
                else:
                    return redirect(novo_estabelecimento)  # Redireciona para a criação de um novo estabelecimento

                
    else:
        return render(request, 'login.html')

        
def logout(request):
    logout_django(request)
    return render(request,'logout.html')
    
    
    