class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo Insuficiente")
        else:
            self.saldo -= valor

conta = ContaBancaria("Mayquel")
conta.depositar(100)
conta.sacar(30)
print(conta.saldo)
