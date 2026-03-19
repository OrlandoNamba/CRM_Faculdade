from core_clientes.services import (
    cadastrar_cliente,
    obter_cliente_por_cpf,
    obter_todos_clientes,
    atualizar_cliente_service,
    deletar_cliente_service
)

from core_clientes.cliente_utils import mostrar_cliente


while True:
    print("\n===== CRM =====")
    print("1 - Inserir Cliente")
    print("2 - Listar Clientes")
    print("3 - Buscar Cliente")
    print("4 - Atualizar Cliente")
    print("5 - Deletar Cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # =========================
    # INSERIR
    # =========================
    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o CPF do cliente: ")
        cidade = input("Digite a cidade do cliente: ")
        telefone = input("Digite o telefone do cliente: ")

        resultado = cadastrar_cliente(nome, cpf, cidade, telefone)

        if resultado == "sucesso":
            print("Cliente cadastrado com sucesso!")
            cliente = obter_cliente_por_cpf(cpf)
            mostrar_cliente(cliente)

        elif resultado == "cpf_invalido":
            print("CPF inválido.")

        elif resultado == "telefone_invalido":
            print("Telefone inválido.")

        elif resultado == "cpf_existente":
            print("CPF já cadastrado.")

    # =========================
    # LISTAR
    # =========================
    elif opcao == "2":
        clientes = obter_todos_clientes()

        if not clientes:
            print("Nenhum cliente encontrado.")
        else:
            for cliente in clientes:
                mostrar_cliente(cliente)

    # =========================
    # BUSCAR
    # =========================
    elif opcao == "3":
        cpf = input("Digite o CPF do cliente: ")
        cliente = obter_cliente_por_cpf(cpf)

        if cliente:
            mostrar_cliente(cliente)
        else:
            print("Cliente não encontrado.")

    # =========================
    # ATUALIZAR
    # =========================
    elif opcao == "4":
        cpf = input("Digite o CPF do cliente: ")
        cliente = obter_cliente_por_cpf(cpf)

        if not cliente:
            print("Cliente não encontrado.")
        else:
            print("Cliente encontrado:")
            mostrar_cliente(cliente)

            nome = input("Novo nome (ENTER para manter): ")
            cidade = input("Nova cidade (ENTER para manter): ")
            telefone = input("Novo telefone (ENTER para manter): ")

            # mantém valores antigos se vazio
            nome = nome if nome else cliente["nome"]
            cidade = cidade if cidade else cliente["cidade"]
            telefone = telefone if telefone else cliente["telefone"]

            resultado = atualizar_cliente_service(
                cliente["id_cliente"],
                nome,
                cliente["cpf"],  # mantém CPF original
                cidade,
                telefone
            )

            if resultado == "sucesso":
                print("Cliente atualizado com sucesso.")
            elif resultado == "cpf_invalido":
                print("CPF inválido.")
            elif resultado == "telefone_invalido":
                print("Telefone inválido.")
            elif resultado == "cpf_existente":
                print("CPF já cadastrado.")

    # =========================
    # DELETAR
    # =========================
    elif opcao == "5":
        cpf = input("Digite o CPF do cliente: ")
        cliente = obter_cliente_por_cpf(cpf)

        if not cliente:
            print("Cliente não encontrado.")
        else:
            print("Cliente encontrado:")
            mostrar_cliente(cliente)

            confirmacao = input("Tem certeza que deseja deletar? (s/n): ")

            if confirmacao.lower() == "s":
                resultado = deletar_cliente_service(cpf)

                if resultado == "sucesso":
                    print("Cliente deletado com sucesso.")
                elif resultado == "cpf_invalido":
                    print("CPF inválido.")
                elif resultado == "nao_encontrado":
                    print("Cliente não encontrado.")
            else:
                print("Operação cancelada.")

    # =========================
    # SAIR
    # =========================
    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida.")