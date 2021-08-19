class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('a', '@')

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('Refrigerante', 6)
p1.desconto(10)
print(f'{p1.nome}, {p1.preco:.2f}')

p2 = Produto('Caneca', 'R$16')
p2.desconto(5)
print(f'{p2.nome}, {p2.preco:.2f}')
