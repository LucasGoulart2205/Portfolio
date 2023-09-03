notaUm=float(input("Qual a primeira  nota?"))
notaDois=float(input("Qual a segunda  nota?"))
notaTres=float(input("Qual a terceira  nota?"))
 
media= (notaUm + notaDois + notaTres) / 3
conceito=0
aprovacao=0

if media >= 9:
    conceito='A'
elif media >= 7.5 and media <9:
    conceito='B'
elif media >=6 and media < 7.5:
    conceito="C"
elif media >= 4 and media < 6:
    conceito='D'
else: conceito = 'F'
 
if conceito == 'A' or conceito== 'B' or  conceito=='C':
    aprovacao='APROVADO'
else: aprovacao='REPROVADO'
print(f'A sua primeira nota foi: {notaUm}\n Sua segunda nota foi: {notaDois}\n Sua terceira nota foi:{notaTres}\n Seu conceito foi: {conceito}\n {aprovacao}')
