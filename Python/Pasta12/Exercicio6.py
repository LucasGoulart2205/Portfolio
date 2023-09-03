#FUP para ler e escrever três números. 
#Se o primeiro for positivo, imprimir sua raiz quadrada, caso contrário, imprimir o seu quadrado; 
# se o segundo número for maior que 10 e menor que 100, imprimir a mensagem: "NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO"; 
# se o terceiro número for menor que o segundo, calcular e escrever a diferença entre eles, caso contrário, calcular e escrever a soma entre eles. 

from cmath import sqrt


print("Exercicio 6")

num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite outro número:'))
if num1 > 0:
    raiz = float (num1) ** 0.5
    print (f'{raiz}')
else:
     quadrado: num1 * num1
     print (f'{raiz}')
if num2 > 10 and num2 < 100:
    print ('Esta entre 10 e 100')    
if num3 < num2: 
    diferenca = num3 - num2 
    print (f'A diferença entre {num3} e {num2} é: {diferenca}')
else:
    soma = num3 + num2
    print (f'A Soma entre {num3} e {num2} é: {soma}')