frutas = ["maçã", "banana", "uva"]

print(frutas[0])    # maçã (o índice começa em 0, como no Java)
print(frutas[-1])   # uva (índice negativo conta do fim!)
print(len(frutas))  # 3 (equivale ao .size() do Java)

frutas.append("jaca")
frutas.insert(0,"manga")
frutas.remove("banana")
frutas[1] = "pera"


print(frutas)

for fruta in frutas:
    print(fruta)

if "uva" in frutas:
    print("Tem Uva")