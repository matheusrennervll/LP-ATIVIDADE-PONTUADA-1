import os
os.system('cls')

operacao = input("Operação (+, -, *, /): ")
A = int(input("Valor A: "))
B = int(input("Valor B: "))

if operacao == '+':
    print(A + B)
elif operacao == '-':
    print(A - B)
elif operacao == '*':
    print(A * B)
elif operacao == '/':
    print(A / B)
