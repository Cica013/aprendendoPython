class Banco:
    def __init__(self):
        self.agencia = [1111, 2222, 3333]
        self.conta = []
        self.cliente = []

    def inserirConta(self, valor):
        self.conta.append(valor)

    def inserirCliente(self, valor):
        self.cliente.append(valor)

    def autenticar(self, cliente):
        if cliente not in self.cliente:
            return False
        if cliente.conta not in self.conta:
            return False
        if cliente.conta.agencia not in self.agencia:
            return False

        return True
