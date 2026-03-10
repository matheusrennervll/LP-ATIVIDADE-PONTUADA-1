import os
os.system('cls')

cor = input("Digite a cor do CD: ")

if cor == "verde" or cor == "Verde":
    preco = 10.00
elif cor == "azul" or cor == "Azul":
    preco = 20.00
elif cor == "amarelo" or cor == "Amarelo":
    preco = 30.00
elif cor == "vermelho" or cor == "Vermelho":
    preco = 40.00
else:
    preco = 0.00

if preco > 0:
    print(f"O preço do CD é R$ {preco:.2f}")
else:
    print("Cor inválida.")