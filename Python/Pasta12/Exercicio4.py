#FUP que leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

print("Exercicio 4")

number = float(input("Digite um numero:"))
if number % 2 == 0:
    print(f"Esse número é par.")
else:
    print(f"Seu numero nao é par.")

if number > 0:
    print(f"Seu numero é positivo.")
else:
    print(f"Seu numero é negativo.")