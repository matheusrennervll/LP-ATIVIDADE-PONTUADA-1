import os
os.system('cls')

nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))


total_bruto = quantidade * preco_unitario


if quantidade <= 5:
    taxa_desconto = 0.02  
elif quantidade <= 10:    
    taxa_desconto = 0.03 
else:                   
    taxa_desconto = 0.05  

valor_desconto = total_bruto * taxa_desconto
total_a_pagar = total_bruto - valor_desconto


print("\n--- Resumo da Compra ---")
print(f"Produto: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total_bruto:.2f}")
print(f"Desconto ({taxa_desconto * 100:.0f}%): R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")