import sqlite3
from conexao import conectar_banco
from inserir_cliente import inserir_cliente

conexao = conectar_banco() # Chama a função "conectar_banco" para obter a conexão com o banco de dados e armazena a conexão na variável "conexao"
cursor = conexao.cursor() # Cria um cursor para executar comandos SQL, e armazena o cursor na variável "cursor"

while True: # Inicia um loop infinito para exibir o menu e processar as opções do usuário
    print("\n===== CRM =====")
    print("1 - Inserir Cliente")
    print("2 - Listar Clientes")
    print("3 - Buscar Cliente")
    print("4 - Atualizar Cliente")
    print("5 - Deletar Cliente")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ") # Solicita ao usuário que escolha uma opção do menu e armazena a entrada na variável "opcao"

    if opcao == "1":
        inserir_cliente() # Chama a função "inserir_cliente" para inserir um novo cliente no banco de dados
    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        pass
    elif opcao == "6":
        print("Saindo do programa...")
        break # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Tente novamente.")
