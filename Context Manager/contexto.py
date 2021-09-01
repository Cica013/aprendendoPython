# class Arquivo:
#     def __init__(self, arquivo, modo):
#         print('Abrindo arquivo')
#         self.arquivo = open(arquivo, modo)
#
#     def __enter__(self):
#         print('Retornando arquivo')
#         return self.arquivo
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Fechando arquivo')
#         # Aqui nós vamos tratar a exceção
#         self.arquivo.close()
#
#
# with Arquivo('abc.txt', 'w') as arquivo:
#     arquivo.write('Alguma coisa')
###############################################################
from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
