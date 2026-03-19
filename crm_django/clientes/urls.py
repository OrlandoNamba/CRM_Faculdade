from django.urls import path
from .views import cadastrar_cliente_view, editar_cliente_view, listar_clientes_view

urlpatterns = [
    path('clientes/', listar_clientes_view),
    path('clientes/cadastrar/', cadastrar_cliente_view),
    path('clientes/editar/<str:cpf>/', editar_cliente_view)
]