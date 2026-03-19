from django.urls import path
from .views import listar_clientes_view

urlpatterns = [
    path('clientes/', listar_clientes_view),
]