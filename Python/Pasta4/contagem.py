#Escreva um algoritmo que leia valores inteiros indeterminadamente, para cada leitura deve ser informado se o número é par ou ímpar, o programa se encerra ao ser digitado o número 0. Ao encerrar o programa deve exibir:
#A Soma de todos os valores pares
#A quantidade de todos os valores impares.
impar= 0
par= 0
numero=int(input("Digite um numero: "))
while True:

    if (numero % 2) ==0:
         print("O numero é par")
         par = numero + par
    elif (numero % 2) != 0:
        print("O numero é impar")
        impar += 1
    numero=int(input("Digite um numero inteiro: "))
    if (numero < 1):
         print(f'Voce digitou 0 para encerrar o programa.')
         print(f'A soma de todos os valores pares sao: {par}.')
         print(f'A quantidade de valores impares sao: {impar}.')
         break