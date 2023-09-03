#efetue um programa que mostre todos os números inteiros ímpares situados na faixa de 1000 a 1500. 
# Esse algoritmo deve ser feito duas vezes, uma usando o FOR,WHILE;

print('Atividade 2')

x=1001
while x <1500:
   print(x)
   x= x + 2

x=1001
for i in range(2,501,2):
     print(x)
     x=x+2