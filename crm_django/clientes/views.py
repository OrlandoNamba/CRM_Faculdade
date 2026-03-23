from django.shortcuts import render, redirect
from django.contrib import messages
from core_clientes.services import obter_todos_clientes
from core_clientes.services import cadastrar_cliente
from core_clientes.services import obter_cliente_por_cpf, atualizar_cliente_service
from core_clientes.services import deletar_cliente_service

def listar_clientes_view(request):
    clientes = obter_todos_clientes()

    cpf_aleatorio = None

    if clientes:
        import random
        cliente_aleatorio = random.choice(clientes)
        cpf_aleatorio = cliente_aleatorio['cpf']

    return render(request, 'clientes/listar_clientes.html', 
                  {'clientes': clientes, 
                   'cpf_aleatorio': cpf_aleatorio}
    )

def cadastrar_cliente_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        telefone2 = request.POST.get('telefone2')
        telefone3 = request.POST.get('telefone3')
        renda = request.POST.get('renda')
        data_nascimento = request.POST.get('data_nascimento')
        logradouro = request.POST.get('logradouro')
        bairro = request.POST.get('bairro')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')

        resultado = cadastrar_cliente(nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep)

        if resultado == "sucesso":
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('/clientes/')

        elif resultado == "cpf_invalido":
            messages.error(request, "CPF inválido.")

        elif resultado == "telefone_invalido":
            messages.error(request, "Telefone inválido.")

        elif resultado == "cpf_existente":
            messages.error(request, "CPF já cadastrado.")

        # ESSENCIAL
        return render(request, 'clientes/cadastrar_clientes.html')

    return render(request, 'clientes/cadastrar_clientes.html')

def editar_cliente_view(request, cpf):
    cliente = obter_cliente_por_cpf(cpf)

    if not cliente:
        return redirect('/clientes/')
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')

        resultado = atualizar_cliente_service(
            cliente['id_cliente'],
            nome,
            cliente['cpf'],
            cidade,
            telefone
        )

        if resultado == "sucesso":
            return redirect('/clientes/')
        
        return render(request, 'clientes/editar_clientes.html', {
            'cliente': cliente,
            'erro': resultado
        })
    return render(request, 'clientes/editar_clientes.html', {
        'cliente': cliente
    })

def deletar_cliente_view(request, cpf):
    if request.method == 'POST':
        deletar_cliente_service(cpf)
        return redirect('/clientes/')
    
def detalhes_cliente_view(request, cpf):
    cliente = obter_cliente_por_cpf(cpf)

    if not cliente:
        return redirect('/clientes/')

    clientes = obter_todos_clientes()

    anterior = None
    proximo = None

    for i, c in enumerate(clientes):
        if c['cpf'] == cpf:
            if i > 0:
                anterior = clientes[i - 1]
            if i < len(clientes) - 1:
                proximo = clientes[i + 1]
            break

    return render(request, 'clientes/detalhes_cliente.html', {
        'cliente': cliente,
        'anterior': anterior,
        'proximo': proximo
    })