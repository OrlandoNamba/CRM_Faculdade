from database.conexao import conectar_banco
from cliente_utils import mostrar_cliente

def buscar_cliente(cpf = None):
    conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

    if cpf is None:
        cpf = input("Digite o CPF do cliente: ") 

    cursor.execute("SELECT * FROM clientes WHERE cpf = ?",
                (cpf,)) # Executa um comando SQL para selecionar o cliente com o CPF especificado, usando um parâmetro para evitar SQL injection

    cliente = cursor.fetchone() # Armazena o resultado da consulta na variável "cliente"

    if cliente:
        mostrar_cliente(cliente) 
    else:
        print("Cliente não encontrado.")

    conexao.close() # Fecha a conexão com o banco de dados

if __name__ == "__main__":
    buscar_cliente()