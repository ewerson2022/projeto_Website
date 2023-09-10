from django.contrib import admin

from estabelecimento.models import Estabelecimento, Loja


class estabecimentos( admin.ModelAdmin):
    list_display= ('numero_estabelecimento', 'razao_social', 'cnpj', 'endereco' )
    

    

admin.site.register( Estabelecimento, estabecimentos)
def __str__(self) -> str:
    return self.razao_social

class lojas(admin.ModelAdmin):
    list_display = ('numero_loja', 'razao_social', 'endereco', 'estabelecimento' )
    
    
    
admin.site.register(Loja, lojas)
def __str__(self) -> str:
    return self.razao_social