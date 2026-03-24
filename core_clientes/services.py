from datetime import datetime
import sqlite3
from database.conexao import conectar_banco
from validacoes.validacoes import validar_cpf, validar_telefone
from core_clientes.repository import deletar_cliente_por_cpf, inserir_cliente
from core_clientes.repository import buscar_cliente_por_cpf
from core_clientes.repository import listar_todos_clientes
from core_clientes.repository import atualizar_cliente

def cadastrar_cliente(nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep):

    if not validar_cpf(cpf):
        return "cpf_invalido"

    if not validar_telefone(telefone):
        return "telefone_invalido"
    
    resultado = inserir_cliente(nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep)

    return resultado

def obter_cliente_por_cpf(cpf):
    cliente = buscar_cliente_por_cpf(cpf)

    if cliente:
        cliente = dict(cliente)  # CONVERTE sqlite3.Row → dict

        if cliente['data_nascimento']:
            cliente['data_nascimento'] = datetime.strptime(
                cliente['data_nascimento'], "%Y-%m-%d"
            ).strftime("%d/%m/%Y")

    return cliente

def obter_todos_clientes():
    clientes = listar_todos_clientes()

    lista_clientes = []

    for cliente in clientes:
        cliente = dict(cliente)

        if cliente['data_nascimento']:
            cliente['data_nascimento'] = datetime.strptime(
                cliente['data_nascimento'], "%Y-%m-%d"
            ).strftime("%d/%m/%Y")

        lista_clientes.append(cliente)

    return clientes

def atualizar_cliente_service(id_cliente, nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep):
    if not validar_cpf(cpf):
        return "cpf_invalido"

    if not validar_telefone(telefone):
        return "telefone_invalido"
    
    resultado = atualizar_cliente(id_cliente, nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep)

    return resultado

def deletar_cliente_service(cpf):
    return deletar_cliente_por_cpf(cpf)
