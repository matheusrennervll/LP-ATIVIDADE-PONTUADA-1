import os
os.system('cls')

num1=int(input('Digite o número que deseja:'))
num2=int(input('Digite o número que deseja:'))
num3=int(input('Digite o número que deseja:'))

soma=num1 + num2

if soma < num3:
    print(f'a soma({soma}) do primeiro número ({num1}) mais segundo número ({num2}) é menor que o terceiro número ({num3}')
elif soma > num3:
    print(f'a soma ({soma}) do primeiro número ({num1}) mais o segundo número ({num2}) é maior que o terceiro número ({num3}')