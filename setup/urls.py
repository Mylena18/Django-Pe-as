"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('fornecedores/', views.fornecedor_list, name='fornecedor_list'),
    path('fornecedores/novo/', views.fornecedor_create, name='fornecedor_create'),
    path('fornecedores/editar/<int:pk>/', views.fornecedor_update, name='fornecedor_update'),
    path('fornecedores/excluir/<int:pk>/', views.fornecedor_delete, name='fornecedor_delete'),

    path('pecas/', views.peca_list, name='peca_list'),
    path('pecas/novo/', views.peca_create, name='peca_create'),
    path('pecas/editar/<int:pk>/', views.peca_update, name='peca_update'),
    path('pecas/excluir/<int:pk>/', views.peca_delete, name='peca_delete'),
]
