gastos = [45.90, 120.00, 32.50, 89.90, 55.00]

total_gasto = sum(gastos)
maior_gasto =  max(gastos)

print(f"O total de Gastos é {total_gasto:.2f}")
print(f"O Maior de Gasto é {maior_gasto}")

qtde_acima_50 = 0

for gasto in gastos:
    if gasto > 50:
        qtde_acima_50 += 1


print(f"A quantidade maior que 50 é {qtde_acima_50}")

#nova versão
qtde_acima_50 = len([g for g in gastos if g > 50])