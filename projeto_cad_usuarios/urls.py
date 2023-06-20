from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # página inicial será vazia ''
    path('', views.home,name='home'),

    #listagem usuários
    path('usuarios/', views.usuarios,name='listagem_usuarios'),
]
