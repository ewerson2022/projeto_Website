from django.contrib import messages
from django.contrib.messages import constants  
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from estabelecimento.models import EstabelecimentoForm, Estabelecimento, Loja, LojaForm
from django.shortcuts import render, get_object_or_404, redirect


# crud Estabelecimento

@login_required
def novo_estabelecimento(request):
      
      if request.method == "POST":
         numero_estabelecimento  = request.POST.get('número do estabecimento')
         razao_social = request.POST.get('razão social')
         cnpj = request.POST.get('cnpj')
         endereco = request.POST.get('endereço')
         
         if  not numero_estabelecimento.strip():
            #messages.error(request,'o campo numero_est não pode ficar vazio')
            return redirect(novo_estabelecimento)
        
         if not razao_social.strip():
           # messages.error(request,'o campo razão social não pode ficar vazio')
            return redirect(novo_estabelecimento)
         
         
         if not cnpj.strip():
           # messages.error(request,'o campo CNPJ não pode ficar vazio')
            return redirect(novo_estabelecimento)
         
         if not endereco.strip():
           # messages.error(request,'o campo endereço não pode ficar vazio')
            return redirect(novo_estabelecimento)
         
        
         if Estabelecimento.objects.filter(cnpj=cnpj).exists():
           # messages.add_message(request, constants.WARNING, 'Já existe um usuario com esse cnpj')
            return redirect(novo_estabelecimento)
        
        
         try:
      
               usuario_estabelecimento = Estabelecimento.objects.create(numero_estabelecimento=numero_estabelecimento,
                                                                        razao_social=razao_social,
                                                                        cnpj=cnpj,
                                                                        endereco=endereco,
                                                                        user=request.user)
               usuario_estabelecimento.save()
               
              
               return redirect(listar_estabelecimento)
            
         except:    
               messages.add_message(request, constants.ERROR, 'ERRO NO SISTEMA')
               return redirect(listar_estabelecimento)
      else:
         return render(request,'estabelecimento_form.html')

@login_required
def listar_estabelecimento(request):
  
   usuario_estabelecimento = Estabelecimento.objects.filter(user=request.user)
   return render(request, 'estabelecimento_list.html', {'usuario_estabelecimentos': usuario_estabelecimento})

@login_required
def editar_estabelecimento(request, estabelecimento_id):
   
    estabelecimento = get_object_or_404(Estabelecimento, id=estabelecimento_id)

    if request.method == 'POST':
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            form.save()
            return redirect(reverse('estabelecimento_listar'))
    else:
        form = EstabelecimentoForm(instance=estabelecimento)

    return render(request, 'estabelecimento_edit.html', {'form': form})

@login_required
def excluir_estabelecimento(request, estabelecimento_id):
    estabelecimento = get_object_or_404(Estabelecimento, id=estabelecimento_id)
    
    if request.method == 'POST':
        resposta = request.POST.get('excluir')
        if resposta == 'sim':
            estabelecimento.delete()
      #      messages.add_message(request, constants.SUCCESS, 'Estabelecimento apagado com sucesso.')
            return redirect('estabelecimento_listar')
        else:
      #      messages.add_message(request, constants.SUCCESS, 'Exclusão cancelada.')
            return redirect('estabelecimento_listar')
    else:
        context = {'estabelecimento': estabelecimento}
        return render(request, 'estabelecimento_excluir.html', context)

#==============================================================================================================================

# crud da Loja

 
@login_required
def nova_loja(request, estabelecimento_id):
   estabelecimento = get_object_or_404(Estabelecimento, id=estabelecimento_id)
    
   if request.method == 'POST':
      numero_loja = request.POST.get('numero_loja')
      razao_social = request.POST.get('razão social')
      endereco = request.POST.get('endereço')
      estabelecimento = estabelecimento
    
      if  not numero_loja.strip():
   #            messages.error(request,'o campo numero_est não pode ficar vazio')
               return redirect(nova_loja)
         
      if not razao_social.strip():
 #              messages.error(request,'o campo razão social não pode ficar vazio')
               return redirect(nova_loja)
            
      if not endereco.strip():
 #              messages.error(request,'o campo endereço não pode ficar vazio')
               return redirect(nova_loja)
            
   
         
      
      try:
            usuario_loja = Loja.objects.create(numero_loja=numero_loja,
                                               razao_social=razao_social,
                                               endereco=endereco,
                                               estabelecimento = estabelecimento)      
            usuario_loja.save()
            
            
  #          messages.add_message(request, constants.SUCCESS, 'LOJA CADASTRADA COM SUCESSO')
            return redirect(reverse(listar_loja,args=[estabelecimento_id]))
            
      except:
    #        messages.add_message(request, constants.ERROR, 'ERRO NO SISTEMA')
            return redirect(reverse(listar_loja,args=[estabelecimento_id]))
 
   else:
         
         return render(request,'nova_loja.html')
 
@login_required
def listar_loja(request, estabelecimento_id):
   
    usuario_loja = Loja.objects.filter(estabelecimento_id=estabelecimento_id)
    return render(request, 'loja_list.html', {'usuario_loja': usuario_loja})
 
@login_required
def editar_loja(request, loja_id):
    loja = get_object_or_404(Loja, id=loja_id)
    estabelecimento_id = loja.estabelecimento.id

    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
  #          messages.success(request, 'Loja atualizada com sucesso.')
            return redirect(reverse('listar_loja', args=[estabelecimento_id]))

    else:
      form =LojaForm(instance=loja)

    return render(request, 'loja_edit.html', {'form': form})     
   
@login_required  
def excluir_loja(request, loja_id):
    loja = get_object_or_404(Loja, id=loja_id)
    estabelecimento_id = loja.estabelecimento.id
    
    if request.method == 'POST':
        resposta = request.POST.get('excluir')
        if resposta == 'sim':
            loja.delete()
  #          messages.add_message(request, constants.SUCCESS, 'Loja apagada com sucesso.')
            return redirect(reverse('listar_loja', args=[estabelecimento_id]))
        else:
    #        messages.add_message(request, constants.SUCCESS, 'Exclusão cancelada.')
            return redirect(reverse('listar_loja', args=[estabelecimento_id]))
    else:
        context = {'loja': loja}
        return render(request, 'loja_excluir.html', context)
