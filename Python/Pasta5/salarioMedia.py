mulherAcima200=0
salariomedia=0
menoridade=100
for i in range (3):
    idade=float(input("Digite sua idade: "))
    sexo=(input("Digite seu sexo: "))
    salario=int(input("Digite seu salario: "))

    if sexo == 'mulher' and salario < 200:
        mulherAcima200 += 1
print(mulherAcima200)

i=0
if i<1:
        salariomedia +=salario
        media= (salariomedia) / 3

if idade < menoridade:
    menoridade == idade
    print(menoridade)