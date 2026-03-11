import sqlite3
from conexao import conectar_banco

conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

cursor.execute("""
INSERT INTO clientes (nome, cpf, cidade, telefone) 
VALUES (?, ?, ?, ?)
""", ("João Silva", "12345678901", "São Paulo", "1199999999")) #Executa um comando SQL para inserir um novo cliente na tabela "clientes" com os valores especificos

conexao.commit() #Salva as alterações no banco de dados
conexao.close() #Fecha a conexão com o banco de dados
