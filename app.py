import tkinter as tk
from tkinter import ttk, messagebox
from conexao import conectar


def cadastrar_cliente():
    nome = entrada_nome_cliente.get()
    telefone = entrada_telefone_cliente.get()
    email = entrada_email_cliente.get()

    if nome == "":
        messagebox.showwarning("Atenção", "Digite o nome do cliente.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO clientes (nome, telefone, email)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()

    cursor.close()
    conexao.close()

    entrada_nome_cliente.delete(0, tk.END)
    entrada_telefone_cliente.delete(0, tk.END)
    entrada_email_cliente.delete(0, tk.END)

    listar_clientes()
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")


def listar_clientes():
    for item in tabela_clientes.get_children():
        tabela_clientes.delete(item)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_cliente, nome, telefone, email FROM clientes")
    clientes = cursor.fetchall()

    for cliente in clientes:
        tabela_clientes.insert("", tk.END, values=cliente)

    cursor.close()
    conexao.close()


def cadastrar_produto():
    nome = entrada_nome_produto.get()
    categoria = entrada_categoria_produto.get()
    preco_custo = entrada_custo_produto.get()
    preco_venda = entrada_venda_produto.get()
    estoque = entrada_estoque_produto.get()

    if nome == "" or preco_venda == "" or estoque == "":
        messagebox.showwarning("Atenção", "Preencha os campos obrigatórios.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos 
    (nome, categoria, preco_custo, preco_venda, estoque)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, categoria, preco_custo, preco_venda, estoque))
    conexao.commit()

    cursor.close()
    conexao.close()

    entrada_nome_produto.delete(0, tk.END)
    entrada_categoria_produto.delete(0, tk.END)
    entrada_custo_produto.delete(0, tk.END)
    entrada_venda_produto.delete(0, tk.END)
    entrada_estoque_produto.delete(0, tk.END)

    listar_produtos()
    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")


def listar_produtos():
    for item in tabela_produtos.get_children():
        tabela_produtos.delete(item)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, nome, categoria, preco_custo, preco_venda, estoque
        FROM produtos
    """)

    produtos = cursor.fetchall()

    for produto in produtos:
        tabela_produtos.insert("", tk.END, values=produto)

    cursor.close()
    conexao.close()


def cadastrar_vendedor():
    nome = entrada_nome_vendedor.get()
    telefone = entrada_telefone_vendedor.get()
    email = entrada_email_vendedor.get()

    if nome == "":
        messagebox.showwarning("Atenção", "Digite o nome do vendedor.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO vendedores (nome, telefone, email)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nome, telefone, email))
    conexao.commit()

    cursor.close()
    conexao.close()

    entrada_nome_vendedor.delete(0, tk.END)
    entrada_telefone_vendedor.delete(0, tk.END)
    entrada_email_vendedor.delete(0, tk.END)

    listar_vendedores()
    messagebox.showinfo("Sucesso", "Vendedor cadastrado com sucesso!")


def listar_vendedores():
    for item in tabela_vendedores.get_children():
        tabela_vendedores.delete(item)

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_vendedor, nome, telefone, email FROM vendedores")
    vendedores = cursor.fetchall()

    for vendedor in vendedores:
        tabela_vendedores.insert("", tk.END, values=vendedor)

    cursor.close()
    conexao.close()


janela = tk.Tk()
janela.title("Sistema de Vendas - Interface Gráfica")
janela.geometry("950x600")
janela.configure(bg="#f4f6f8")

abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")


# ABA CLIENTES
aba_clientes = ttk.Frame(abas)
abas.add(aba_clientes, text="Clientes")

tk.Label(aba_clientes, text="Cadastro de Clientes", font=("Arial", 18, "bold")).pack(pady=10)

frame_cliente = tk.Frame(aba_clientes)
frame_cliente.pack(pady=10)

tk.Label(frame_cliente, text="Nome").grid(row=0, column=0)
entrada_nome_cliente = tk.Entry(frame_cliente, width=30)
entrada_nome_cliente.grid(row=0, column=1, padx=5)

tk.Label(frame_cliente, text="Telefone").grid(row=1, column=0)
entrada_telefone_cliente = tk.Entry(frame_cliente, width=30)
entrada_telefone_cliente.grid(row=1, column=1, padx=5)

tk.Label(frame_cliente, text="Email").grid(row=2, column=0)
entrada_email_cliente = tk.Entry(frame_cliente, width=30)
entrada_email_cliente.grid(row=2, column=1, padx=5)

tk.Button(frame_cliente, text="Cadastrar Cliente", command=cadastrar_cliente).grid(row=3, column=1, pady=10)

colunas_clientes = ("ID", "Nome", "Telefone", "Email")
tabela_clientes = ttk.Treeview(aba_clientes, columns=colunas_clientes, show="headings")

for coluna in colunas_clientes:
    tabela_clientes.heading(coluna, text=coluna)

tabela_clientes.pack(expand=True, fill="both", padx=20, pady=10)


# ABA PRODUTOS
aba_produtos = ttk.Frame(abas)
abas.add(aba_produtos, text="Produtos")

tk.Label(aba_produtos, text="Cadastro de Produtos", font=("Arial", 18, "bold")).pack(pady=10)

frame_produto = tk.Frame(aba_produtos)
frame_produto.pack(pady=10)

tk.Label(frame_produto, text="Nome").grid(row=0, column=0)
entrada_nome_produto = tk.Entry(frame_produto, width=30)
entrada_nome_produto.grid(row=0, column=1, padx=5)

tk.Label(frame_produto, text="Categoria").grid(row=1, column=0)
entrada_categoria_produto = tk.Entry(frame_produto, width=30)
entrada_categoria_produto.grid(row=1, column=1, padx=5)

tk.Label(frame_produto, text="Preço Custo").grid(row=2, column=0)
entrada_custo_produto = tk.Entry(frame_produto, width=30)
entrada_custo_produto.grid(row=2, column=1, padx=5)

tk.Label(frame_produto, text="Preço Venda").grid(row=3, column=0)
entrada_venda_produto = tk.Entry(frame_produto, width=30)
entrada_venda_produto.grid(row=3, column=1, padx=5)

tk.Label(frame_produto, text="Estoque").grid(row=4, column=0)
entrada_estoque_produto = tk.Entry(frame_produto, width=30)
entrada_estoque_produto.grid(row=4, column=1, padx=5)

tk.Button(frame_produto, text="Cadastrar Produto", command=cadastrar_produto).grid(row=5, column=1, pady=10)

colunas_produtos = ("ID", "Nome", "Categoria", "Custo", "Venda", "Estoque")
tabela_produtos = ttk.Treeview(aba_produtos, columns=colunas_produtos, show="headings")

for coluna in colunas_produtos:
    tabela_produtos.heading(coluna, text=coluna)

tabela_produtos.pack(expand=True, fill="both", padx=20, pady=10)


# ABA VENDEDORES
aba_vendedores = ttk.Frame(abas)
abas.add(aba_vendedores, text="Vendedores")

tk.Label(aba_vendedores, text="Cadastro de Vendedores", font=("Arial", 18, "bold")).pack(pady=10)

frame_vendedor = tk.Frame(aba_vendedores)
frame_vendedor.pack(pady=10)

tk.Label(frame_vendedor, text="Nome").grid(row=0, column=0)
entrada_nome_vendedor = tk.Entry(frame_vendedor, width=30)
entrada_nome_vendedor.grid(row=0, column=1, padx=5)

tk.Label(frame_vendedor, text="Telefone").grid(row=1, column=0)
entrada_telefone_vendedor = tk.Entry(frame_vendedor, width=30)
entrada_telefone_vendedor.grid(row=1, column=1, padx=5)

tk.Label(frame_vendedor, text="Email").grid(row=2, column=0)
entrada_email_vendedor = tk.Entry(frame_vendedor, width=30)
entrada_email_vendedor.grid(row=2, column=1, padx=5)

tk.Button(frame_vendedor, text="Cadastrar Vendedor", command=cadastrar_vendedor).grid(row=3, column=1, pady=10)

colunas_vendedores = ("ID", "Nome", "Telefone", "Email")
tabela_vendedores = ttk.Treeview(aba_vendedores, columns=colunas_vendedores, show="headings")

for coluna in colunas_vendedores:
    tabela_vendedores.heading(coluna, text=coluna)

tabela_vendedores.pack(expand=True, fill="both", padx=20, pady=10)


listar_clientes()
listar_produtos()
listar_vendedores()

janela.mainloop()