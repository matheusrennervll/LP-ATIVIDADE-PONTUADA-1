import os
os.system('cls')

renda = float(input("Renda mensal: "))
valor_total = float(input("Valor do empréstimo: "))
parcelas = int(input("Nº de prestações: "))

valor_parcela = valor_total / parcelas
limite_total = renda * 10
limite_parcela = renda * 0.30

print(f"\nParcela: R$ {valor_parcela:.2f} (Máx: R$ {limite_parcela:.2f})")
print(f"Total: R$ {valor_total:.2f} (Máx: R$ {limite_total:.2f})")

if valor_total <= limite_total and valor_parcela <= limite_parcela:
    print("\nResultado: Empréstimo CONCEDIDO!")
else:
    print("\nResultado: Empréstimo NEGADO.")
    if valor_total > limite_total:
        print("- Motivo: Valor total excede 10x a renda.")
    if valor_parcela > limite_parcela:
        print("- Motivo: Parcela excede 30% da renda.")
