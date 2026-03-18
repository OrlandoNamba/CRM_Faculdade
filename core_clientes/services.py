import sqlite3
from database.conexao import conectar_banco
from validacoes.validacoes import validar_cpf, validar_telefone
from core_clientes.repository import deletar_cliente_por_cpf, inserir_cliente
from core_clientes.repository import buscar_cliente_por_cpf
from core_clientes.repository import listar_todos_clientes
from core_clientes.repository import atualizar_cliente

def cadastrar_cliente(nome, cpf, cidade, telefone):

    if not validar_cpf(cpf):
        return "cpf_invalido"

    if not validar_telefone(telefone):
        return "telefone_invalido"
    
    resultado = inserir_cliente(nome, cpf, cidade, telefone)

    return resultado

def obter_cliente_por_cpf(cpf):
    cliente = buscar_cliente_por_cpf(cpf)
    return cliente

def obter_todos_clientes():
    clientes = listar_todos_clientes()
    return clientes

def atualizar_cliente_service(id_cliente, nome, cpf, cidade, telefone):
    if not validar_cpf(cpf):
        return "cpf_invalido"

    if not validar_telefone(telefone):
        return "telefone_invalido"
    
    resultado = atualizar_cliente(id_cliente, nome, cpf, cidade, telefone)

    return resultado

def deletar_cliente_service(cpf):
    if not validar_cpf(cpf):
        return "cpf_invalido"

    resultado = deletar_cliente_por_cpf(cpf)
    return resultado