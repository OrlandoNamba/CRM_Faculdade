# Responsável pela conexão com o banco SQLite do CRM

import sqlite3

def conectar_banco():
    conexao = sqlite3.connect('database/crm.db') # Conecta ao banco de dados "crm.db", e armazena a conexão na variável "conexao"
    conexao.row_factory = sqlite3.Row # Configura a conexão para retornar os resultados das consultas como objetos do tipo "Row", permitindo acessar os campos por nome
    return conexao # Retorna a conexão com o banco de dados

def atualizar_tabela_clientes():
    conexao = conectar_banco() # Estabelece a conexão com o banco de dados
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL

    try:
        cursor.execute("ALTER TABLE clientes ADD COLUMN telefone2 VARCHAR(15)")
    except:
        pass
    
    try:
        cursor.execute("ALTER TABLE clientes ADD COLUMN telefone3 VARCHAR(15)")
    except:
        pass
    
    try:
        cursor.execute("ALTER TABLE clientes ADD COLUMN renda DECIMAL(10,2)")
    except:
        pass

    conexao.commit() # Salva as alterações no banco de dados
    conexao.close() # Fecha a conexão com o banco de dados