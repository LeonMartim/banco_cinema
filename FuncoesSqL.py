import pyodbc

def colectar():

    conn_str = (
        r"Driver={SQL Server};"
        r"Server=.\SQLEXPRESS02;"
        r"Database=cinema;"
        r"Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

def inserir_filme(cursor, nome, data_lancamento, orcamento, tempo):
    sql = "INSERT INTO Filme (nome_filme, data_lancamento, orcamento, tempo) VALUES (?, ?, ?, ?)"
    cursor.execute(sql, (nome,  data_lancamento, orcamento, tempo))

def listar_filmes(cursor):
    cursor.execute("SELECT * FROM Filme")
    return cursor.fetchall()

def listar_personagem(cursor):
    cursor.execute("SELECT * FROM Personagem")
    return cursor.fetchall()

def deletar_filme(cursor, cod_filme):
    try:
        cursor.execute("DELETE FROM Filme WHERE cod_filme = ?", (cod_filme,))
        if cursor.rowcount:
            return True
        else:
            return False
        
    except Exception as f:
        print(f"Erro ao tentar deletar filme: {f}\n")
        return False


def deletar_personagem(cursor, cod_personagem):
    try:
        cursor.execute("DELETE FROM Personagem WHERE cod_personagem = ?", (cod_personagem,))
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as p:
        print(f"Erro ao tentar deletar Personagem: {p}\n")
        return False
