import os
os.system('cls')

kg_mo = float(input("Kg de morangos: "))
kg_ma = float(input("Kg de maçãs: "))


val_mo = kg_mo * (2.50 if kg_mo <= 5 else 2.20)
val_ma = kg_ma * (1.80 if kg_ma <= 5 else 1.50)

valor_total = val_mo + val_ma
peso_total = kg_mo + kg_ma


if peso_total >= 10 or valor_total > 15.00:
    valor_total *= 0.90

print(f"Valor final a pagar: R$ {valor_total:.2f}")