import mysql.connector
from mysql.connector import Error

# """Cria uma conexão com o banco de dados MySQL."""
def create_connection(host, user, password, db):
    conn = None
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        if conn.is_connected():
          print("Conectado ao MySQL")
        else:
          print('Falha ao conectar ao MySQL')
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    return conn

# """Cria um cursor a partir de uma conexão existente."""
def create_cursor(connection):
    cursor = None
    try:
        cursor = connection.cursor()
        print("Cursor criado com sucesso")
    except Error as e:
        print(f"Erro ao criar o cursor: {e}")
    return cursor
  
# """Executa uma consulta no banco de dados MySQL."""
def execute_query(connection, query):
    cursor = create_cursor(connection)
    try:
        cursor.execute(query)
        connection.commit()
        print("Consulta executada com sucesso")
    except Error as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        cursor.close()

# """Executa uma consulta de seleção e retorna os resultados."""
def fetch_query_results(connection, query):
    cursor = create_cursor(connection)
    results = None
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print("Consulta de seleção executada com sucesso")
    except Error as e:
        print(f"Erro ao executar a consulta de seleção: {e}")
    finally:
        cursor.close()
    return results
