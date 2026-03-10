import sqlite3

conexao = sqlite3.connect('database/crm.db') #Conecta ao banco de dados "crm.db", e armazena a conexão na variável "conexao"
cursor = conexao.cursor() #Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

cursor.execute("SELECT * FROM clientes") #Executa um comando SQL para selecionar todos os registros da tabela "clientes"
clientes = cursor.fetchall() #Armazena os resultados da consulta na variável "clientes"

for cliente in clientes:
    print(cliente) #Cada cliente vai ser mostrado como tupla

conexao.close() #Fecha a conexão com o banco de dados