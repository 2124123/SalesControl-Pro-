from clientes import cadastrar_cliente
from produtos import cadastrar_produto
from vendedores import cadastrar_vendedor, listar_vendedores
from vendas import registrar_venda
from relatorios import gerar_relatorio_vendas

def menu():
    while True:
        print("\n===== SISTEMA DE VENDAS =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Cadastrar Vendedor")
        print("4 - Listar Vendedores")
        print("5 - Registrar Venda")
        print("6 - Gerar Relatório Excel")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cadastrar_cliente(nome, telefone, email)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            preco_custo = float(input("Preço de custo: "))
            preco_venda = float(input("Preço de venda: "))
            estoque = int(input("Quantidade em estoque: "))
            cadastrar_produto(nome, categoria, preco_custo, preco_venda, estoque)

        elif opcao == "3":
            nome = input("Nome do vendedor: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cadastrar_vendedor(nome, telefone, email)

        elif opcao == "4":
            listar_vendedores()

        elif opcao == "5":
            id_cliente = int(input("ID do cliente: "))
            id_vendedor = int(input("ID do vendedor: "))
            id_produto = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            forma_pagamento = input("Forma de pagamento: ")

            registrar_venda(
                id_cliente,
                id_vendedor,
                id_produto,
                quantidade,
                forma_pagamento
            )

        elif opcao == "6":
            gerar_relatorio_vendas()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()