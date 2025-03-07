import os
os.system ("clear")

primeiro_valor = float(input("Digite o Primeiro Valor:"))
segundo_valor = float(input("Digite o Segundo Valor:"))
terceiro_valor = float(input("Digite o Terceiro Valor:"))
       
if primeiro_valor + segundo_valor < terceiro_valor:
 print()
 print("A soma do Primeiro Valor e do Segundo é Menor que o Terceiro")
else:
 primeiro_valor + segundo_valor >terceiro_valor
 print("A Soma do Primeiro Valor e do Segundo é Maior que o Terceiro")


print(f"soma do primeiro e segundo:{primeiro_valor + segundo_valor}")
print(f"terceiro valor:{terceiro_valor}")