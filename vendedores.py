from conexao import conectar

def cadastrar_vendedor(nome, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO vendedores (nome, telefone, email)
    VALUES (%s, %s, %s)
    """

    valores = (nome, telefone, email)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Vendedor cadastrado com sucesso!")


def listar_vendedores():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM vendedores")
    vendedores = cursor.fetchall()

    for v in vendedores:
        print(f"ID: {v[0]} | Nome: {v[1]} | Telefone: {v[2]} | Email: {v[3]}")

    cursor.close()
    conexao.close()


def buscar_vendedor(id_vendedor):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM vendedores WHERE id_vendedor = %s", (id_vendedor,))
    vendedor = cursor.fetchone()

    cursor.close()
    conexao.close()

    return vendedor


def atualizar_vendedor(id_vendedor, nome, telefone, email):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE vendedores
    SET nome = %s, telefone = %s, email = %s
    WHERE id_vendedor = %s
    """

    cursor.execute(sql, (nome, telefone, email, id_vendedor))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Vendedor atualizado com sucesso!")


def deletar_vendedor(id_vendedor):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM vendedores WHERE id_vendedor = %s", (id_vendedor,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("Vendedor excluído com sucesso!")