import sqlite3
from conexao import conectar_banco

conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor" 

cursor.execute("SELECT * FROM clientes") #Executa um comando SQL para selecionar todos os registros da tabela "clientes"
clientes = cursor.fetchall() #Armazena os resultados da consulta na variável "clientes"

for cliente in clientes:
    print(cliente) #Cada cliente vai ser mostrado como tupla

conexao.close() #Fecha a conexão com o banco de dados