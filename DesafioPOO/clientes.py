from contas import Cp, Cc


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Clientes(Pessoa,):
    pass
