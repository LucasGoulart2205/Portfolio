#Faça um algoritmo que leia um valor inteiro (que representa o real, moeda nacional) e 
#calcule qual o menor número possível de notas de 100, 50, 10, 5, 2 e 1 em que o valor lido pode ser decomposto. 
#Escrever o valor lido e a relação de notas necessárias, 
#por exemplo: R$ 153 serão decompostos em 1 nota de R$100, 1 nota de R$ 50, 1 nota de R$ 2 e 1 nota de R$ 1.

valor=int(input("Digite um valor: "))
total = valor
moeda= 100
totalmoeda=0
while True:
    if total >= moeda:
         total -= moeda
         totalmoeda += 1
    else:
        if totalmoeda > 0:
            print(f'Decomposto em {totalmoeda} nota de R$ {moeda}')
        elif moeda == 100:
                moeda = 50
        elif moeda == 50:
                moeda =10
        elif moeda == 10:
                moeda = 5
        elif moeda == 5:
                moeda =2
        elif moeda == 2:
                moeda = 1
        totalmoeda=0
        if total == 0:
            break