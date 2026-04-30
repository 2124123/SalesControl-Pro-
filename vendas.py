from conexao import conectar

def registrar_venda(id_cliente, id_vendedor, id_produto, quantidade, forma_pagamento):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT preco_venda, estoque FROM produtos WHERE id_produto = %s", (id_produto,))
    produto = cursor.fetchone()

    if produto is None:
        print("Produto não encontrado.")
        return

    preco_venda, estoque = produto

    if estoque < quantidade:
        print("Estoque insuficiente.")
        return

    subtotal = preco_venda * quantidade

    cursor.execute("""
        INSERT INTO vendas 
        (id_cliente, id_vendedor, forma_pagamento, valor_total)
        VALUES (%s, %s, %s, %s)
    """, (id_cliente, id_vendedor, forma_pagamento, subtotal))

    id_venda = cursor.lastrowid

    cursor.execute("""
        INSERT INTO itens_venda 
        (id_venda, id_produto, quantidade, preco_unitario, subtotal)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_venda, id_produto, quantidade, preco_venda, subtotal))

    cursor.execute("""
        UPDATE produtos 
        SET estoque = estoque - %s
        WHERE id_produto = %s
    """, (quantidade, id_produto))

    conexao.commit()

    cursor.close()
    conexao.close()

    print("Venda registrada com sucesso!")