class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self.nome

    @property
    def idade(self):
        return self.idade

    @nome.setter
    def nome(self, valor):
        self.nome = valor
        return

    @idade.setter
    def idade(self, valor):
        self.idade = valor
        return


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

        self.conta = None

    def inserirConta(self, valor):
        self.conta = valor



