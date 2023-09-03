#2 - Cada cigarro consumido, o fumante perde em média 15 minutos de vida. 
#Faça um algoritmo que leia quantos cigarros são consumidos pelo usuário diariamente e há quanto tempo e fumante em meses.  Considere que cada 
# mês tenha 30 dias.
#Ao fim mostre quanto tempo ele perderá de vida segundo os dados de entrada.  
#E conforme o tempo que o usuário fuma, mostrar as consequências.

#Se ele fuma há um tempo menor ou igual a 90 dias,  dentes amarelos.
#Tempo entre 90 e 365 dias, perda de paladar e respiração comprometida. 
#Mais que 365 dias, pulmão comprometido.

diarimante=float(input("Digite quantos cigarros voce fuma diariamente: "))
meses=float(input("Digite em meses ha quanto tempo voce fuma: "))
tempo= (meses * diarimante) * 15
if meses <= 3:
    print(f'Dentes amarelos')
if meses >3 and meses <12 :
    print(f'Perda de paladar e respiraçao comprometida')
if meses > 12 :
    print(f'pulmao comprometido')

print(f'voce perdeu {tempo} minutos de vida')