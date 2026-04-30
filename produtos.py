from conexao import conectar

def cadastrar_produto(nome, categoria, preco_custo, preco_venda, estoque):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos 
    (nome, categoria, preco_custo, preco_venda, estoque)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (nome, categoria, preco_custo, preco_venda, estoque)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Produto cadastrado com sucesso!")