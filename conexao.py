# Responsável pela conexão com o banco SQLite do CRM

import sqlite3

def conectar_banco():
    conexao = sqlite3.connect('database/crm.db') # Conecta ao banco de dados "crm.db", e armazena a conexão na variável "conexao"
    conexao.row_factory = sqlite3.Row # Configura a conexão para retornar os resultados das consultas como objetos do tipo "Row", permitindo acessar os campos por nome
    return conexao # Retorna a conexão com o banco de dados