from conexao import conectar_banco
from inserir_cliente import inserir_cliente
from listar_clientes import listar_clientes

while True: # Inicia um loop infinito para exibir o menu e processar as opções do usuário
    print("\n===== CRM =====")
    print("1 - Inserir Cliente")
    print("2 - Listar Clientes")
    print("3 - Buscar Cliente")
    print("4 - Atualizar Cliente")
    print("5 - Deletar Cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ") # Solicita ao usuário que escolha uma opção do menu e armazena a entrada na variável "opcao"

    if opcao == "1":
        inserir_cliente()
    elif opcao == "2":
        listar_clientes() 
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        pass
    elif opcao == "0":
        print("Saindo do programa...")
        break # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Tente novamente.")
