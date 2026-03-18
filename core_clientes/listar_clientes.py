from database.conexao import conectar_banco
from core_clientes.cliente_utils import mostrar_cliente

def listar_clientes():
    conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor" 

    cursor.execute("SELECT * FROM clientes") #Executa um comando SQL para selecionar todos os registros da tabela "clientes"
    clientes = cursor.fetchall() #Armazena os resultados da consulta na variável "clientes"

    if not clientes:
        print("Nenhum cliente encontrado.")

    else:
        for cliente in clientes:
            mostrar_cliente(cliente)

    conexao.close()

if __name__ == "__main__":
    listar_clientes()