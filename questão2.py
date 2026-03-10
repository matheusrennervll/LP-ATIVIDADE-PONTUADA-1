import os
os.system('cls')

# ENTRADA

nome=input('Digite seu nome: ')
sexo=input('Qual o seu sexo: ')
estado_civil=input('Qual o seu estado civil: ')

# PROCESSAMENTO

if sexo == 'F' and estado_civil == 'casada':
    tempo=input('quanto tempo de casada?:')
    print(f'seu nome é {nome} \no seu sexo é {sexo} \nseu estado civil é {estado_civil} \no seu tempo de casada é {tempo} ')

# SÁIDA

else:

    print('------ENTÃO------')
    print(f'seu nome é {nome} \no seu sexo é {sexo} \nseu estado civil é {estado_civil}')
 
