import sqlite3
from database.conexao import conectar_banco

def inserir_cliente(nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO clientes (nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep))

        conexao.commit()
        return "sucesso"

    except sqlite3.IntegrityError:
        return "cpf_existente"

    finally:
        conexao.close()

def buscar_cliente_por_cpf(cpf):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
        cliente = cursor.fetchone()
        return cliente
    finally:
        conexao.close()

def listar_todos_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return clientes
    
    except sqlite3.Error:
        return None

    finally:
        conexao.close()

def atualizar_cliente(id_cliente, nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE clientes 
        SET nome = ?, cpf = ?, cidade = ?, telefone = ?, telefone2 = ?, telefone3 = ?, renda = ?, data_nascimento = ?, logradouro = ?, bairro = ?, estado = ?, cep = ?
        WHERE id_cliente = ?
        """, (nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep, id_cliente))

        conexao.commit()

        if cursor.rowcount == 0:
            return "cliente_nao_encontrado"

        return "sucesso"

    except sqlite3.IntegrityError:
        return "cpf_existente"

    finally:
        conexao.close()

def deletar_cliente_por_cpf(cpf):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))
        conexao.commit()

        if cursor.rowcount == 0:
            return "cliente_nao_encontrado"

        return "sucesso"

    finally:
        conexao.close()