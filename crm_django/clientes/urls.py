from django.urls import path
from .views import (
    cadastrar_cliente_view,
    criar_usuario_view,
    detalhes_cliente_view,
    editar_cliente_view,
    excluir_usuario_view,
    listar_clientes_view,
    deletar_cliente_view,
    login_view,
    logout_view,
    tornar_admin_view
)

urlpatterns = [
    path('clientes/', listar_clientes_view, name='listar_clientes'),
    path('clientes/cadastrar/', cadastrar_cliente_view, name='cadastrar_cliente'),
    path('clientes/editar/<int:id_cliente>/', editar_cliente_view, name='editar_cliente'),
    path('clientes/deletar/<int:id_cliente>/', deletar_cliente_view, name='deletar_cliente'),
    path('clientes/detalhes/<int:id_cliente>/', detalhes_cliente_view, name='detalhes_cliente'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', login_view, name='home'),

    path('usuarios/criar/', criar_usuario_view, name='criar_usuario'),
    path('usuarios/admin/<int:user_id>/', tornar_admin_view, name='tornar_admin'),
    path('usuarios/excluir/<int:user_id>/', excluir_usuario_view, name='excluir_usuario'),
]