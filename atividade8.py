import os
os.system("clear")

cor = input("Digite a cor do CD: ")

if cor == "Vermelho":
    preco = 40.00
elif cor == "Azul":
    preco = 20.00
elif cor == "Verde":
    preco = 10.00
elif cor == "Amarelo":
    preco = 30.00
else:
    preco = "Cor inválida"

print(f"O preço do CD é: {preco}")
