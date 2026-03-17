import sqlite3
from database.conexao import conectar_banco
from validacoes.validacoes import validar_cpf, validar_telefone

def cadastrar_cliente(nome, cpf, cidade, telefone):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    if not validar_cpf(cpf):
        conexao.close()
        return "cpf_invalido"

    if not validar_telefone(telefone):
        conexao.close()
        return "telefone_invalido"

    try:
        cursor.execute("""
        INSERT INTO clientes (nome, cpf, cidade, telefone) 
        VALUES (?, ?, ?, ?)
        """, (nome, cpf, cidade, telefone))

        conexao.commit()
        conexao.close()
        return "sucesso"

    except sqlite3.IntegrityError:
        conexao.close()
        return "cpf_existente"