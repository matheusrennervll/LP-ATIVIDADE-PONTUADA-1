import os
os.system('cls')

operacao = input("Digite a operação desejada (+, -, *, /): ")
A = int(input("Digite o valor do número inteiro A: "))
B = int(input("Digite o valor do número inteiro B: "))

if operacao == '+':
    resultado = A + B
    print(f"\nResultado: {A} {operacao} {B} = {resultado}")

elif operacao == '-':
    resultado = A - B
    print(f"\nResultado: {A} {operacao} {B} = {resultado}")

elif operacao == '*':
    resultado = A * B
    print(f"\nResultado: {A} {operacao} {B} = {resultado}")

elif operacao == '/':

    if B == 0:
        print("\nErro: Não é possível dividir um número por zero.")
    else:
        resultado = A / B
        print(f"\nResultado: {A} {operacao} {B} = {resultado}")

else:
    print("\nErro: Operação inválida. Por favor, digite +, -, * ou /.")
