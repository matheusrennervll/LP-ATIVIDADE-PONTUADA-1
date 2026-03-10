import os
os.system('cls')

preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ")

valor_a_pagar = 0


if tipo == 'A' or tipo == 'a':
  
    valor_bruto = litros * preco_alcool
    if litros <= 20:
        desconto = 0.03  
    else:
        desconto = 0.05  
    
    valor_a_pagar = valor_bruto - (valor_bruto * desconto)

elif tipo == 'G' or tipo == 'g':
  
    valor_bruto = litros * preco_gasolina
    if litros <= 20:
        desconto = 0.04  
    else:
        desconto = 0.06  
        
    valor_a_pagar = valor_bruto - (valor_bruto * desconto)

else:
    print("Erro: Tipo de combustível inválido!")

if valor_a_pagar > 0:
    print("\n--- Resumo do Abastecimento ---")
    
    if tipo == 'A' or tipo == 'a':
        nome_combustivel = "Álcool"
    else:
        nome_combustivel = "Gasolina"
        
    print(f"Combustível: {nome_combustivel}")
    print(f"Litros: {litros:.2f}L")
    print(f"Total a pagar: R$ {valor_a_pagar:.2f}")