# Responsável pela conexão com o banco SQLite do CRM

import sqlite3

def conectar_banco():
    conexao = sqlite3.connect('database/crm.db') # Conecta ao banco de dados "crm.db", e armazena a conexão na variável "conexao"
    return conexao # Retorna a conexão com o banco de dados