# Trabalhando com list comprehension

string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[v:v + n]for v in range(0, len(string), n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)
