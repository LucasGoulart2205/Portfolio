#Elabore um programa que calcule e escreva a soma de 10 números lidos.Esse algorimo deve ser feito três vezes uma usando o FOR e WHILE

print('Atividade 1')
adicao=0
for x in range (10):
    numero=(int(input('Digite um numero :')))
    adicao= adicao + numero
    print(adicao)
    
adicao=0
soma_total=0

while adicao < 10:
    numero=int(input("Digite um numero: "))
    soma_total += numero
    adicao+=1

print (soma_total)