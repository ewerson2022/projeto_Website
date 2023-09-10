
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticacao/',include('cadastro.urls')),
    path("", lambda request: redirect('login')),
    path('home/', include('estabelecimento.urls')),
    
    
    
]
