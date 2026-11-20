class Gasto:
    def __init__(self, descricao, valor, categoria):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
    def mostrar(self):
        print(f"{self.categoria} - {self.descricao}: {self.valor}")

g = Gasto("Compras do mês", 155.00, "Mercado")
g.mostrar()

lista_gasto = [Gasto("Compras do mês", 155.00, "Mercado"),Gasto("Combustível", 855.00, "Carro"), Gasto("Agua", 85.00, "Contas Casa")]

for gasto in lista_gasto:
    gasto.mostrar()