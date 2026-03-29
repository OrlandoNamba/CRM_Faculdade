import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core_clientes.services import obter_todos_clientes
from core_clientes.services import cadastrar_cliente
from core_clientes.services import obter_cliente_por_cpf, atualizar_cliente_service, obter_cliente_por_id
from core_clientes.repository import marcar_interesse, remover_interesse, liberar_cliente, listar_todos_clientes
from datetime import datetime, timedelta
from core_clientes.services import deletar_cliente_service
from datetime import datetime

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/clientes/')

    next_url = request.GET.get('next', '/clientes/')

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        next_url = request.POST.get('next', '/clientes/')

        user = authenticate(request, username=username, password=senha)

        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('/login/')

# ========================================
# FUNÇÃO AUXILIAR (IMPORT PROFISSIONAL)
# ========================================
def pegar_valor_coluna(linha, *nomes):
    for nome in nomes:
        if nome in linha:
            valor = linha[nome]
            if pd.notna(valor):
                return valor
    return None

@login_required
def listar_clientes_view(request):
    clientes = listar_todos_clientes()
    clientes_filtrados = []

    for cliente in clientes:

        interessado = cliente.get('interessado')
        usuario_interesse = cliente.get('usuario_interesse')
        data_interesse = cliente.get('data_interesse')

        # Cliente livre
        if not interessado:
            clientes_filtrados.append(cliente)
            continue

        # Admin vê tudo
        if request.user.is_superuser:
            clientes_filtrados.append(cliente)
            continue

        # Usuário dono do interesse
        if usuario_interesse == request.user.id:
            clientes_filtrados.append(cliente)
            continue

        # Verificar se passou 5 dias
        if data_interesse:
            data_interesse = datetime.strptime(
                data_interesse,
                "%Y-%m-%d %H:%M:%S"
            )

            if datetime.now() > data_interesse + timedelta(days=5):
                liberar_cliente(cliente['id_cliente'])
                clientes_filtrados.append(cliente)

    return render(request, 'clientes/listar_clientes.html', {
        'clientes': clientes_filtrados
    })

@login_required
def cadastrar_cliente_view(request):
    if request.method == 'POST':

        # =============================
        # IMPORTAÇÃO POR EXCEL
        # =============================
        if 'arquivo_excel' in request.FILES:
            arquivo = request.FILES['arquivo_excel']

            try:
                df = pd.read_excel(arquivo)
                df.columns = df.columns.str.lower().str.strip()

                sucessos = 0
                erros = 0
                erros_detalhados = []

                for _, linha in df.iterrows():

                    nome = pegar_valor_coluna(
                        linha, 'nome', 'nome_cliente', 'cliente'
                    )

                    cpf = pegar_valor_coluna(
                        linha, 'cpf', 'documento', 'cpf_cliente'
                    )

                    telefone = pegar_valor_coluna(
                        linha, 'telefone', 'celular', 'fone', 'telefone1', 'contato'
                    )

                    cidade = pegar_valor_coluna(
                        linha, 'cidade', 'municipio'
                    )

                    telefone2 = pegar_valor_coluna(
                        linha, 'telefone2', 'telefone_2', 'celular2', 'contato2'
                    )

                    telefone3 = pegar_valor_coluna(
                        linha, 'telefone3', 'telefone_3', 'celular3', 'contato3'
                    )

                    renda = pegar_valor_coluna(
                        linha, 'renda', 'salario', 'remuneracao'
                    )

                    data_nascimento = pegar_valor_coluna(
                        linha, 'data_nascimento', 'nascimento', 'data nascimento', 'aniversario'
                    )

                    logradouro = pegar_valor_coluna(
                        linha, 'logradouro', 'endereco', 'rua'
                    )

                    bairro = pegar_valor_coluna(
                        linha, 'bairro'
                    )

                    estado = pegar_valor_coluna(
                        linha, 'estado', 'uf'
                    )

                    cep = pegar_valor_coluna(
                        linha, 'cep'
                    )

                    # =============================
                    # TRATAMENTO EXCEL
                    # =============================
                    if cpf:
                        cpf = str(cpf)
                        cpf = cpf.replace('.0', '')
                        cpf = cpf.replace('.', '')
                        cpf = cpf.replace('-', '')
                        cpf = cpf.replace(' ', '')
                        cpf = cpf.strip()

                    if telefone:
                        telefone = str(telefone)
                        telefone = telefone.replace('.0', '')
                        telefone = telefone.replace(' ', '')
                        telefone = telefone.replace('-', '')
                        telefone = telefone.replace('(', '')
                        telefone = telefone.replace(')', '')

                    if data_nascimento:
                        data_nascimento = str(data_nascimento).split(' ')[0]

                    resultado = cadastrar_cliente(
                        nome, cpf, cidade, telefone,
                        telefone2, telefone3, renda,
                        data_nascimento, logradouro,
                        bairro, estado, cep
                    )

                    if resultado == "sucesso":
                        sucessos += 1
                    else:
                        erros += 1

                        if resultado == "cpf_invalido":
                            erros_detalhados.append(f"CPF inválido - {nome} - {cpf}")

                        elif resultado == "telefone_invalido":
                            erros_detalhados.append(f"Telefone inválido - {nome} - {telefone}")

                        elif resultado == "cpf_existente":
                            erros_detalhados.append(f"CPF já cadastrado - {nome} - {cpf}")

                        else:
                            erros_detalhados.append(f"Erro desconhecido - {nome} - {cpf}")

                # =============================
                # MENSAGENS
                # =============================
                if sucessos == 0:
                    messages.error(
                        request,
                        f"Importação mal sucedida. {erros} registros com erro."
                    )

                elif erros == 0:
                    messages.success(
                        request,
                        f"Importação realizada com sucesso! {sucessos} clientes importados."
                    )

                else:
                    messages.warning(
                        request,
                        f"Importação concluída com avisos. {sucessos} importados, {erros} erros."
                    )

                # MOSTRAR ERROS DETALHADOS
                for erro in erros_detalhados:
                    messages.error(request, erro)

                return redirect('/clientes/')

            except Exception as e:
                messages.error(request, f"Erro ao importar Excel: {e}")
                return render(request, 'clientes/cadastrar_clientes.html')

        # =============================
        # CADASTRO MANUAL
        # =============================
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

        resultado = cadastrar_cliente(
            nome, cpf, cidade, telefone,
            telefone2, telefone3, renda,
            data_nascimento, logradouro,
            bairro, estado, cep
        )

        if resultado == "sucesso":
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('/clientes/')

        elif resultado == "cpf_invalido":
            messages.error(request, "CPF inválido.")

        elif resultado == "telefone_invalido":
            messages.error(request, "Telefone inválido.")

        elif resultado == "cpf_existente":
            messages.error(request, "CPF já cadastrado.")

        return render(request, 'clientes/cadastrar_clientes.html')

    return render(request, 'clientes/cadastrar_clientes.html')

@login_required
def editar_cliente_view(request, id_cliente):
    cliente = obter_cliente_por_id(id_cliente)

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

@login_required
def deletar_cliente_view(request, id_cliente):
    if request.method == 'POST':
        deletar_cliente_service(id_cliente)
        return redirect('/clientes/')

@login_required
def detalhes_cliente_view(request, id_cliente):
    cliente = obter_cliente_por_id(id_cliente)

    if not cliente:
        return redirect('/clientes/')

    # NOVA PARTE — salvar interesse
    if request.method == 'POST':
        interesse = request.POST.get('interesse')

        if interesse == 'on':
            marcar_interesse(cliente['id_cliente'], request.user.id)
        else:
            remover_interesse(cliente['id_cliente'])

        return redirect(f'/clientes/detalhes/{cliente["id_cliente"]}/')

    # Parte que você já tinha (anterior / próximo)
    clientes = obter_todos_clientes()

    anterior = None
    proximo = None

    for i, c in enumerate(clientes):
        if c['id_cliente'] == id_cliente:
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

@login_required
def criar_usuario_view(request):
    if not request.user.is_superuser:
        return redirect('listar_clientes')

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        admin = request.POST.get('admin')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
        else:
            user = User.objects.create_user(
                username=username,
                password=senha
            )

            if admin == 'on':
                user.is_superuser = True
                user.is_staff = True
                user.save()

            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('criar_usuario')

    usuarios = User.objects.all().order_by('username')

    return render(request, 'criar_usuario.html', {
        'usuarios': usuarios
    })

@login_required
def tornar_admin_view(request, user_id):
    if not request.user.is_superuser:
        return redirect('listar_clientes')

    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)

        if user.is_superuser:
            user.is_superuser = False
            user.is_staff = False
        else:
            user.is_superuser = True
            user.is_staff = True

        user.save()

    return redirect('criar_usuario')


@login_required
def excluir_usuario_view(request, user_id):
    if not request.user.is_superuser:
        return redirect('listar_clientes')

    if request.method == 'POST':
        if request.user.id == user_id:
            messages.error(request, 'Você não pode excluir seu próprio usuário')
            return redirect('criar_usuario')

        user = get_object_or_404(User, id=user_id)
        user.delete()

    return redirect('criar_usuario')