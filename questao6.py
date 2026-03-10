import os
os.system('cls')

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2


print(f"Média do aluno: {media:.1f}")


if media >= 6.0:
    print("Parabéns! Você foi Aprovado.")
elif media >= 4.0: 
    print("O aluno está em Recuperação.")
else:               
    print("O aluno está Reprovado.")