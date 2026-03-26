from django.urls import path
from .views import cadastrar_cliente_view, criar_usuario_view, detalhes_cliente_view, editar_cliente_view, listar_clientes_view, deletar_cliente_view, login_view, logout_view

urlpatterns = [
    path('clientes/', listar_clientes_view, name='listar_clientes'),
    path('clientes/cadastrar/', cadastrar_cliente_view, name='cadastrar_cliente'),
    path('clientes/editar/<str:cpf>/', editar_cliente_view, name='editar_cliente'),
    path('clientes/deletar/<str:cpf>/', deletar_cliente_view, name='deletar_cliente'),
    path('clientes/detalhes/<str:cpf>/', detalhes_cliente_view, name='detalhes_cliente'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', login_view, name='home'),

    path('usuarios/criar/', criar_usuario_view, name='criar_usuario'),
]