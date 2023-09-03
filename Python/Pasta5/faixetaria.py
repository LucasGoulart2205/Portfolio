faixa1=0
faixa2=0
faixa3=0
faixa4=0
faixa5=0


for i in range(0,15):
    idade=int(input("Digite a idade: "))
     
    if idade <= 15:
       faixa1 += 1

    if idade >= 16 and idade <= 30:
        faixa2 += 1

    if idade >= 31 and idade <= 45:
        faixa3 += 1

    if idade >= 46 and idade <= 60:
        faixa4 += 1

    if idade > 60:
        faixa5 += 1

print(f"Pessoas da faixa etaria 1: {faixa1}")
print(f"Pessoas da faixa etaria 2: {faixa2}")
print(f"Pessoas da faixa etaria 3: {faixa3}")
print(f"Pessoas da faixa etaria 4: {faixa4}")
print(f"Pessoas da faixa etaria 5: {faixa5}")

totalDePessoas=(faixa1 + faixa2 + faixa3 + faixa4 + faixa5)
totalfaixa1e5=(faixa1 + faixa5)/ totalDePessoas
porcentagem= (100 * totalfaixa1e5) 
print(f"A porcentagem de pessoas da primeira faixa etaria e da ultima é de {porcentagem}%")



