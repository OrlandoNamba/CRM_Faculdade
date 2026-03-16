from database.conexao import conectar_banco
from clientes.cliente_utils import mostrar_cliente


def atualizar_cliente():
    conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

    cpf = input("Digite o CPF do cliente que deseja atualizar: ")

    cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
                (cpf,))
    cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

    if cliente:
        print("Cliente encontrado:")
        mostrar_cliente(cliente)

        novo_nome = input("Novo Nome (ENTER para manter o atual): ")
        nova_cidade = input("Nova Cidade (ENTER para manter a atual): ")
        novo_telefone = input("Novo Telefone (ENTER para manter o atual): ")
        
        cursor.execute("UPDATE clientes SET nome = ?, cidade = ?, telefone = ? WHERE cpf = ?",
                    (novo_nome, nova_cidade, novo_telefone, cpf)) # Executa um comando SQL para atualizar o telefone do cliente com o CPF especificado, usando parâmetros para evitar SQL injection
        
        conexao.commit() # Salva as alterações no banco de dados
        print("Cliente atualizado com sucesso.")
    else:
        print("Cliente não encontrado")

    conexao.close() # Fecha a conexão com o banco de dados

if __name__ == "__main__":
    atualizar_cliente()