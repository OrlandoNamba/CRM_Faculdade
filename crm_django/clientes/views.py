from django.shortcuts import render
from core_clientes.services import obter_todos_clientes

def listar_clientes_view(request):
    clientes = obter_todos_clientes()

    return render(request, 'clientes/listar_clientes.html', 
                  {'clientes': clientes
    })