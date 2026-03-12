import sqlite3
from conexao import conectar_banco
from buscar_cliente import buscar_cliente

def inserir_cliente():
    
    conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    try:
        cursor.execute("""
        INSERT INTO clientes (nome, cpf, cidade, telefone) 
        VALUES (?, ?, ?, ?)
        """, (nome, cpf, cidade, telefone)) #Executa um comando SQL para inserir um novo cliente na tabela "clientes" com os valores especificos

        conexao.commit()

        print("Cliente cadastrado com sucesso!")
        print("\nCliente cadastrado:")
        buscar_cliente(cpf) # Chama a função "buscar_cliente" para exibir os detalhes do cliente recém-inserido

    except sqlite3.IntegrityError:
        print("Erro: CPF já existe no banco de dados.")

    conexao.close() #Fecha a conexão com o banco de dados

if __name__ == "__main__":
    inserir_cliente()