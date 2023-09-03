idademais50=0
idademais10menos20=0
totalDePessoas=0
totalaltura=0
for i in range(3):
    idade=int(input("Digite sua idade: "))
    altura=float(input("Digite sua altura: "))
    peso=int(input("Digite seu peso: "))
    if idade > 50:
        idademais50 +=1
    if idade >= 10 and idade <= 20:
        idademais10menos20 += 1
        totalaltura += altura
        media= totalaltura / idademais10menos20
    if peso < 40:
        totalDePessoas+= 1
        porcentagem= ( totalDePessoas / 3) * 100 
print(idademais50)
print(media)
print(porcentagem)