import pandas as pd
from conexao import conectar

def gerar_relatorio_vendas():
    conexao = conectar()

    sql = """
    SELECT 
        v.id_venda,
        c.nome AS cliente,
        ve.nome AS vendedor,
        v.data_venda,
        v.forma_pagamento,
        v.valor_total
    FROM vendas v
    INNER JOIN clientes c ON v.id_cliente = c.id_cliente
    INNER JOIN vendedores ve ON v.id_vendedor = ve.id_vendedor
    ORDER BY v.data_venda DESC
    """

    df = pd.read_sql(sql, conexao)

    df.to_excel("relatorio_vendas.xlsx", index=False)

    conexao.close()

    print("Relatório gerado com sucesso!")