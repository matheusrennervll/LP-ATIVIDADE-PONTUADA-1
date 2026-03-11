import os
os.system('cls')

litros = float(input("Quantidade de litros: "))
tipo = input("Tipo (A - Álcool / G - Gasolina): ")

if tipo == 'A' or tipo == 'a':
    nome = "Álcool"
    preco = 3.79
    desconto = 0.03 if litros <= 20 else 0.05
elif tipo == 'G' or tipo == 'g':
    nome = "Gasolina"
    preco = 6.59
    desconto = 0.04 if litros <= 20 else 0.06
else:
    preco = 0 


if preco > 0:
    total = (litros * preco) * (1 - desconto)
    print(f"\nResumo: {nome}")
    print(f"Total: R$ {total:.2f}")
else:
    print("Erro: Tipo inválido!")
