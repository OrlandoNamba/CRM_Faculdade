from django.urls import path
from .views import cadastrar_cliente_view, editar_cliente_view, listar_clientes_view, deletar_cliente_view

urlpatterns = [
    path('clientes/', listar_clientes_view, name='listar_clientes'),
    path('clientes/cadastrar/', cadastrar_cliente_view, name='cadastrar_cliente'),
    path('clientes/editar/<str:cpf>/', editar_cliente_view, name='editar_cliente'),
    path('clientes/deletar/<str:cpf>/', deletar_cliente_view, name='deletar_cliente')
]