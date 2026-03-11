import sqlite3

conexao = sqlite3.connect('database/crm.db') # Conecta ao banco de dados "crm.db", e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

cpf = 12345678901 # CPF do cliente a ser buscado

cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
               (cpf,)) # Executa um comando SQL para selecionar o cliente com o CPF especificado, usando um parâmetro para evitar SQL injection

cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

if cliente:
    print(cliente) # Se o cliente for encontrado, imprime os detalhes do cliente
else:
    print("Cliente não encontrado.") # Se o cliente não for encontrado, imprime uma mensagem indicando que o cliente não foi encontrado

conexao.close() # Fecha a conexão com o banco de dados