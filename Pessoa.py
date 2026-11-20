class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, sou {self.nome}")


p = Pessoa("Mayquel", 40) # sem new
p.apresentar()
print(p.nome)


