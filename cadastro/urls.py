
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('/cadastro/', views.cadastro, name = 'cadastro'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="recuperar.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="resetsant.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="newreset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="confirmation.html"), name="password_reset_complete"), 
]