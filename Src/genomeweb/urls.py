from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Pagina inicial'),
    path(r'gerar_nova_rede/', views.gerar_nova_rede, name='Gerar Nova Rede'),
    path(r'atualizar_politicas/', views.atualizar_politicas, name='Atualizar Rede'),
    path(r'treinar_rede/', views.treinar_rede, name='Treinar Rede'),
]
