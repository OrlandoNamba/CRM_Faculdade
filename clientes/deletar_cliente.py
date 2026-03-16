from database.conexao import conectar_banco

def deletar_cliente():

    conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

    cpf = input("Digite o CPF do cliente que deseja deletar: ")
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
                    (cpf,))
    cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

    if cliente:
        print("\nCliente encontrado:")
        print("Nome", cliente [1])
        print("CPF", cliente [2])
        print("Cidade", cliente [5])
        print("Telefone", cliente [8])

        confirmacao = input("\nTem certeza que deseja deletar este cliente? (s/n): ")
        if confirmacao.lower() == 's':
            cursor.execute("DELETE FROM clientes WHERE cpf = ?",
                        (cpf,)) # Executa um comando SQL para deletar o cliente com o CPF especificado, usando parâmetros para evitar SQL injection
            conexao.commit() # Salva as alterações no banco de dados
            print("Cliente deletado com sucesso.") 
        else:
            print("Operação cancelada.") 
    else:
        print("Cliente não encontrado")