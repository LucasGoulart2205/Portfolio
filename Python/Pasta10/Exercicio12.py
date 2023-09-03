#F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o número. Exiba na tela este valor final.

print("Exercicio 12")

numero1= int(input('Digite um numero:'))
numero2= int(input('Digite um segundo numero:'))

calculo= numero2 % numero1

print(f'O resultado é: {calculo}')