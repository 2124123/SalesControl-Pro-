import streamlit as st
import pandas as pd
from conexao import conectar

st.set_page_config(page_title="Sistema de Vendas", layout="wide")

st.title("Dashboard de Vendas")

conexao = conectar()

df_vendas = pd.read_sql("SELECT * FROM vendas", conexao)
df_produtos = pd.read_sql("SELECT * FROM produtos", conexao)

total_vendas = df_vendas["valor_total"].sum()
qtd_vendas = len(df_vendas)
qtd_produtos = len(df_produtos)

col1, col2, col3 = st.columns(3)

col1.metric("Faturamento Total", f"R$ {total_vendas:.2f}")
col2.metric("Quantidade de Vendas", qtd_vendas)
col3.metric("Produtos Cadastrados", qtd_produtos)

st.subheader("Lista de Vendas")
st.dataframe(df_vendas)

st.subheader("Produtos em Estoque")
st.dataframe(df_produtos)

conexao.close()