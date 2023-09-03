#FUP para efetuar a leitura de quatro números e apresentar os números divisíveis por 2 e por 3.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
numero4 = int(input('Digite o quarto número: '))
 
if numero1 % 2 == 0:
 print(f'O número {numero1} é divisível por 2')
else:
 print(f'O número {numero1} é divisível por 3')
 
if numero2 % 2 == 0:
 print(f'O número {numero2} é divisível por 2')
else:
 print(f'O número {numero2} é divisível por 3')
 
if numero3 % 2 == 0:
 print(f'O número {numero3} é divisível por 2')
else:
 print(f'O número {numero3} é divisível por 3')
 
if numero4 % 2 == 0:
 print(f'O número {numero4} é divisível por 2')
else:
 print(f'O número {numero4} é divisível por 3')
 
