pessoa = {"nome": "Mayquel", "linguagem": "Python", "experiencia": 5}

#print(pessoa["nome"])              # Mayquel (no Java: map.get("nome"))
#print(pessoa.get("idade"))         # None (não existe, mas não dá erro)
#print(pessoa.get("idade", 0))      # 0 (valor padrão, como getOrDefault)


pessoa["cidade"] = "Quatá"       # adiciona (map.put)
pessoa["experiencia"] = 6        # altera
del pessoa["linguagem"]          # remove (map.remove)
#print("nome" in pessoa)          # True (containsKey)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
    
ponto = (10, 20)               # tupla: uma lista que não pode ser alterada
x, y = ponto                   # "desempacota" em duas variáveis

cores = {"azul", "verde", "azul"}
print(cores)                   # {'azul', 'verde'} (set: sem repetidos, como HashSet)


gastos = [45.90, 120.00, 32.50, 89.90, 55.00]

acima_50 = [g for g in gastos if g > 50]     # filtra
com_taxa = [g * 1.1 for g in gastos]         # transforma
print(acima_50)
print(com_taxa)
