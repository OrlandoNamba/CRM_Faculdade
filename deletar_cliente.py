import sqlite3

conexao = sqlite3.connect('database/crm.db') # Conecta ao banco de dados "crm.db", e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

cpf = input("Digite o CPF do cliente que deseja deletar: ") # Solicita ao usuário que digite o CPF do cliente que deseja deletar e armazena a entrada na variável "cpf"
cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
                (cpf,))
cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

if cliente:
    print("\nCliente encontrado:")
    print("Nome", cliente [1])
    print("CPF", cliente [2])
    print("Cidade", cliente [5])
    print("Telefone", cliente [8])

    confirmacao = input("\nTem certeza que deseja deletar este cliente? (s/n): ") # Solicita ao usuário que confirme a exclusão do cliente e armazena a entrada na variável "confirmacao"
    if confirmacao.lower() == 's':
        cursor.execute("DELETE FROM clientes WHERE cpf = ?",
                       (cpf,)) # Executa um comando SQL para deletar o cliente com o CPF especificado, usando parâmetros para evitar SQL injection
        conexao.commit() # Salva as alterações no banco de dados
        print("Cliente deletado com sucesso.") # Imprime uma mensagem indicando que o cliente foi deletado
    else:
        print("Operação cancelada.") # Se o usuário não confirmar a exclusão, imprime uma mensagem indicando que a operação foi cancelada
else:
    print("Cliente não encontrado") # Se o cliente não for encontrado, imprime uma mensagem indicando que o cliente não foi encontrado