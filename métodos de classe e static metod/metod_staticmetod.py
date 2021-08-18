from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Métodos de classes não precisam receber a instância, mas sim a classe em si.
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Métodos estáticos não precisam receber instância nenhuma.
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p = Pessoa.por_ano_nascimento('Luiz', 1995)
print(p.nome, p.idade)
print(Pessoa.gera_id())
print(p.gera_id())
