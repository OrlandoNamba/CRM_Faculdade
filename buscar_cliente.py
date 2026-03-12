from conexao import conectar_banco


def buscar_cliente(cpf = None):
    conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

    if cpf is None:
        cpf = input("Digite o CPF do cliente: ") # Solicita ao usuário que digite o CPF do cliente e armazena a entrada na variável "cpf"

    cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
                (cpf,)) # Executa um comando SQL para selecionar o cliente com o CPF especificado, usando um parâmetro para evitar SQL injection

    cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

    if cliente:
        print(cliente) # Se o cliente for encontrado, imprime os detalhes do cliente
    else:
        print("Cliente não encontrado.") # Se o cliente não for encontrado, imprime uma mensagem indicando que o cliente não foi encontrado

    conexao.close() # Fecha a conexão com o banco de dados