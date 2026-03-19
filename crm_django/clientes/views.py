from django.shortcuts import render, redirect
from core_clientes.services import obter_todos_clientes
from core_clientes.services import cadastrar_cliente

def listar_clientes_view(request):
    clientes = obter_todos_clientes()

    return render(request, 'clientes/listar_clientes.html', 
                  {'clientes': clientes
    })

def cadastrar_cliente_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')

        resultado = cadastrar_cliente(nome, cpf, cidade, telefone)

        if resultado == "sucesso":
            return redirect('/clientes/')
        
        return render(request, 'clientes/cadastrar_clientes.html', {
            'erro': resultado
        })

    return render(request, 'clientes/cadastrar_clientes.html')