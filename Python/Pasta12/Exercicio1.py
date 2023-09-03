#Dados dois números A e B, some 100 ao maior número e imprima.
print("Exercicio 1")

A= int(input("Digite um numero:"))
B= int(input("Digite outro numero:"))

if A>B:
   soma=A+100
else: 
   soma=B+100

print(f'Adicionando 100 ao maior numero fica {soma}')