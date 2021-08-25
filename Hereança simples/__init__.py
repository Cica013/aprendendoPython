# Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
from classes import *

c1 = Cliente('Luiz', 45)
print(c1.nome)
c1.falar()
c1.comprar()

print()
a1 = Aluno('Fernando', 19)
print(a1.nome)
a1.falar()
a1.estudar()
