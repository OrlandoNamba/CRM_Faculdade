from database.conexao import conectar_banco
from clientes.services import cadastrar_cliente
from clientes.listar_clientes import listar_clientes
from clientes.buscar_cliente import buscar_cliente
from clientes.atualizar_cliente import atualizar_cliente
from clientes.deletar_cliente import deletar_cliente
from clientes.cliente_utils import mostrar_cliente

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
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        cidade = input("Digite a cidade do cliente: ")
        telefone = input("Digite o telefone do cliente: ")

        resultado = cadastrar_cliente(nome, cpf, cidade, telefone) # Chama a função "cadastrar_cliente" com os dados fornecidos pelo usuário e armazena o resultado na variável "resultado"

        if resultado == "sucesso":
            print("Cliente cadastrado com sucesso!")
            print("Dados do cliente:")
            buscar_cliente(cpf)

        elif resultado == "cpf_invalido":
            print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")

        elif resultado == "telefone_invalido":
            print("Telefone inválido. O telefone deve conter 10 ou 11 dígitos numéricos.")

        elif resultado == "cpf_existente":
            print("CPF já existente. O CPF fornecido já está cadastrado no sistema.")
            
    elif opcao == "2":
        listar_clientes() 
    elif opcao == "3":
        buscar_cliente()
    elif opcao == "4":
        atualizar_cliente()
    elif opcao == "5":
        deletar_cliente()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
