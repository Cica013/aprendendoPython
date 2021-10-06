import pymysql.cursors
from contextlib import contextmanager


# CRUD - CREATE, READ, UPDATE, DELETE

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()


# INSERE UM REGISTRO NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

# INSERE VARIOS REGISTROS NA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'AMARANTES', 24, 59),
#             ('ANA', 'CLARA', 21, 54),
#             ('FERNANDO', 'AMADO', 32, 86),
#             ('THIAGO', 'VENTURA', 33, 70),
#             ('WELLINGTON', 'ALVEZ', 23, 90),
#             ('JORGE', 'ARAGÃO', 55, 119),
#             ('ARLINDO', 'CRUZ', 70, 85),
#             ('AUGUSTO', 'CARRARA', 55, 62),
#             ('GRAÇA', 'JESUS', 57, 89),
#             ('JOANA', 'DARK', 200, 60),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (8,))
#         conexao.commit()

# DELETA VÁRIOS REGISTROS DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (1, 2, 3))
#         conexao.commit()

# DELETA VÁRIOS REGISTROS DA BASE DE DADOS, MAS DE MODO DIFERENTE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s and %s'
#         cursor.execute(sql, (12, 14))
#         conexao.commit()

# ATUALIZA UM REGISTRO DA BASE DE DADOS
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('PENNY', 19))
#         conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
