#FUP para ler três valores quaisquer e escrever o maior dos 3.
print("Exercicio 9")
num1 = float(input("Digite um primeiro numero:"))
num2 = float(input("Digite um segundo numero:"))
num3 = float(input("Digite um terceiro numero:"))
nummaior= num1

if num2>nummaior:
    nummaior=num2
if num3 > nummaior:
    nummaior=num3

print(f"O maior numero é : {nummaior}")