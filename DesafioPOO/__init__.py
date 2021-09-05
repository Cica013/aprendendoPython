from banco import Banco
from conta import ContaCorrente, ContaPoupanca
from cliente import Cliente

banco = Banco()

cliente1 = Cliente('Silvanis', 26)
cliente2 = Cliente('Islaine', 28)
cliente3 = Cliente('Luiz', 32)

conta1 = ContaPoupanca(1111, 234596, 0)
conta2 = ContaCorrente(2222, 489752, 0)
conta3 = ContaPoupanca(3333, 478521, 0)

cliente1.inserirConta(conta1)
cliente2.inserirConta(conta2)
cliente3.inserirConta(conta3)

cliente1.conta.depositar(40)
cliente1.conta.sacar(10)

