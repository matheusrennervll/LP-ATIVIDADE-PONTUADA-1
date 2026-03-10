import os
os.system('cls')

renda_mensal = float(input("Digite a renda mensal do usuário: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo: "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))


valor_prestacao = valor_emprestimo / num_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

print("\n--- Resumo da Análise ---")
print(f"Valor da prestação: R$ {valor_prestacao:.2f} (Limite permitido: R$ {limite_prestacao:.2f})")
print(f"Valor do empréstimo: R$ {valor_emprestimo:.2f} (Limite permitido: R$ {limite_emprestimo:.2f})")


if valor_emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("\nResultado: Empréstimo CONCEDIDO! ")
else:
    print("\nResultado: Empréstimo NEGADO. ")
    
    if valor_emprestimo > limite_emprestimo:
        print("- Motivo: O valor total solicitado é maior que 10 vezes a renda mensal.")
    if valor_prestacao > limite_prestacao:
        print("- Motivo: O valor da prestação compromete mais de 30% da renda mensal.")