from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pecas, name='lista_pecas'),
    path('nova/', views.criar_peca, name='criar_peca'),
    path('editar/<int:id>/', views.editar_peca, name='editar_peca'),
    path('visualizar/<int:id>/', views.visualizar_peca, name='visualizar_peca'),
    path('deletar/<int:id>/', views.deletar_peca, name='deletar_peca'),
]