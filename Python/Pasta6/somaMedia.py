lista=[]

for i in range(5):
    valor=int(input("Digite o valor inteiro: "))
    lista.append(valor)

for i in range(5):
     print(f'{lista[i]}')

#soma dos elemtos
total=0
for i in range(5):
    total+=lista[i]
print(total)
#media
print(total/5)

#soma tbm
total=sum(lista)
print(total)

i=0
while i<5:
    valor=int(input("Digite o valor inteiro: "))
    lista.append(valor)
    i=+1
i=0
while i < 5:
    print(f'{lista[i]}')