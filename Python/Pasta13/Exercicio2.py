#FUP que lê um conjunto de 4 valores i, a, b, c, onde i é um valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir:
#Se i=1 escrever os 3 valores a, b, c em ordem crescente;
#Se i=2 escrever os 3 valores a, b, c em ordem decrescente;
#Se i=3 escrever os 3 valores de forma que o maior valor entre a, b, c fica entre os outros dois.

i= int(input('digite um valor inteiro:'))
a=float(input('digite outro numero:'))
b=float(input('digite mais um numero:'))
c=float(input('digite o ultimo numero:'))

lista = [a, b, c]

if i == 1:
   lista.sort()
print (f'ordem crescente {lista}')
