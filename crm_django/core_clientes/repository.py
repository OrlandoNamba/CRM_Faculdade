import sqlite3
from database.conexao import conectar_banco


def inserir_cliente(nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO clientes 
        (nome, cpf, cidade, telefone, telefone2, telefone3, renda, data_nascimento, logradouro, bairro, estado, cep) 
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
        colunas = [col[0] for col in cursor.description]
        cliente = cursor.fetchone()

        if cliente:
            return dict(zip(colunas, cliente))
        return None
    finally:
        conexao.close()


def listar_todos_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")
        colunas = [col[0] for col in cursor.description]
        clientes = []

        for linha in cursor.fetchall():
            clientes.append(dict(zip(colunas, linha)))

        return clientes

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


def deletar_cliente_por_id(id_cliente):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM clientes WHERE id_cliente = ?", (id_cliente,))
        conexao.commit()

        if cursor.rowcount == 0:
            return "cliente_nao_encontrado"

        return "sucesso"

    finally:
        conexao.close()


# =========================
# SISTEMA DE INTERESSE
# =========================

def marcar_interesse(id_cliente, user_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE clientes
            SET interessado = 1,
                usuario_interesse = ?,
                data_interesse = datetime('now')
            WHERE id_cliente = ?
        """, (user_id, id_cliente))

        conexao.commit()
        return "sucesso"

    finally:
        conexao.close()


def remover_interesse(id_cliente):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE clientes
            SET interessado = 0,
                usuario_interesse = NULL,
                data_interesse = NULL
            WHERE id_cliente = ?
        """, (id_cliente,))

        conexao.commit()
        return "sucesso"

    finally:
        conexao.close()


def liberar_cliente(id_cliente):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE clientes
            SET interessado = 0,
                usuario_interesse = NULL,
                data_interesse = NULL
            WHERE id_cliente = ?
        """, (id_cliente,))

        conexao.commit()

    finally:
        conexao.close()

def obter_cliente_por_id(id_cliente):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = ?", (id_cliente,))
        colunas = [col[0] for col in cursor.description]
        cliente = cursor.fetchone()

        if cliente:
            return dict(zip(colunas, cliente))
        return None

    finally:
        conexao.close()