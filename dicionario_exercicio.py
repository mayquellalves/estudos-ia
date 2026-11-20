gastos = {
    "mercado": [120.00, 89.90, 45.50],
    "transporte": [32.50, 15.00],
    "lazer": [55.00, 80.00],
    "saude":[280.03, 900.00]
}

totais = {}

for categoria, valores in gastos.items():
    totais[categoria] = sum(valores)

for categoria, total in totais.items():
    print(f"Total em categoria {categoria}: R$ {total:.2f}")

maior_categoria = ""
maior_total = 0

for categoria, total in totais.items():
    if total > maior_total:
        maior_total = total
        maior_categoria = categoria

print(f"Maior gasto: {maior_categoria} (R$ {maior_total:.2f})")

maior_categoria_s = max(totais, key=totais.get)
print(maior_categoria_s)

for categoria, valores in gastos.items():
    acima_50 = [g for g in valores if g > 50 ]
    print(f"{categoria}: {acima_50}")

