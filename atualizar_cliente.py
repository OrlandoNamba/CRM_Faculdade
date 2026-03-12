from conexao import conectar_banco

conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

cpf = input("Digite o CPF do cliente que deseja atualizar: ") # Solicita ao usuário que digite o CPF do cliente que deseja atualizar e armazena a entrada na variável "cpf"

cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
               (cpf,))
cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

if cliente:
    novo_telefone = input("Digite o novo telefone do cliente: ") # Solicita ao usuário que digite o novo telefone do cliente e armazena a entrada na variável "novo_telefone"
    cursor.execute("UPDATE clientes SET telefone = ? WHERE cpf = ?",
                   (novo_telefone, cpf)) # Executa um comando SQL para atualizar o telefone do cliente com o CPF especificado, usando parâmetros para evitar SQL injection
    
    conexao.commit() # Salva as alterações no banco de dados
    print("Telefone atualizado com sucesso.") # Imprime uma mensagem indicando que o telefone foi atualizado
else:
    print("Cliente não encontrado") # Se o cliente não for encontrado, imprime uma mensagem indicando que o cliente não foi encontrado