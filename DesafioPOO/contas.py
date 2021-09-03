class Conta:
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor < self.saldo:
            print('Valor negado!')
            return
        self.saldo -= valor


class Cp(Conta):
    def __init__(self, agencia, conta):
        super().__init__(agencia, conta)


class Cc(Conta):
    def __init__(self, agencia, conta, limite=100):
        super().__init__(agencia, conta)
        self.limite = limite

    def sacar(self, valor):
        if valor < (self.saldo + self.limite):
            print('Valor negado!')
            return
        self.saldo -= valor










