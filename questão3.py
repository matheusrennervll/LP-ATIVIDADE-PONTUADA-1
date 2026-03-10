import os
os.system('cls')

A = int(input("Digite o primeiro valor inteiro (A): "))
B = int(input("Digite o segundo valor inteiro (B): "))


if A == B:
    C = A + B      
else:
    C = A * B      


print(f"O resultado armazenado em C é: {C}")