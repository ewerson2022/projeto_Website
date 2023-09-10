
from django.contrib import admin
from django.urls import path
from estabelecimento.views import *
from . import views



urlpatterns = [
    #paths_estabelecimento
    #==========================================================================================================================
    path('estabelecimento/novo', views.novo_estabelecimento, name= 'estabelecimento novo'),
    path('estabelecimento/listar', views.listar_estabelecimento, name = 'estabelecimento_listar'),
    path('estabelecimento/editar/<int:estabelecimento_id>/', views.editar_estabelecimento, name='editar_estabelecimento'),
    path('estabelecimento/excluir/<int:estabelecimento_id>/', views.excluir_estabelecimento, name = 'excluir_estabelecimento'),
     #=========================================================================================================================
     #paths_loja
    path('estabelecimento/nova_loja/<int:estabelecimento_id>/', views.nova_loja, name= 'nova_loja'),
    path('estabelecimento/listar_loja/<int:estabelecimento_id>/', views.listar_loja, name = 'listar_loja'),
    path('estabelecimento/editar_loja/<int:loja_id>/', views.editar_loja, name = 'editar_loja'),
    path('estabelecimento/excluir_loja/<int:loja_id>/', views.excluir_loja, name = 'excluir_loja'),
]