from conexao import conectar

def cadastrar_cliente(nome, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO clientes (nome, telefone, email)
    VALUES (%s, %s, %s)
    """

    valores = (nome, telefone, email)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id_cliente, nome, telefone, email FROM clientes")
    clientes = cursor.fetchall()

    print("\n===== LISTA DE CLIENTES =====")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Telefone: {cliente[2]} | Email: {cliente[3]}")

    cursor.close()
    conexao.close()


def buscar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_cliente, nome, telefone, email
        FROM clientes
        WHERE id_cliente = %s
    """, (id_cliente,))

    cliente = cursor.fetchone()

    cursor.close()
    conexao.close()

    return cliente


def atualizar_cliente(id_cliente, nome, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE clientes
    SET nome = %s, telefone = %s, email = %s
    WHERE id_cliente = %s
    """

    cursor.execute(sql, (nome, telefone, email, id_cliente))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Cliente atualizado com sucesso!")


def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Cliente excluído com sucesso!")