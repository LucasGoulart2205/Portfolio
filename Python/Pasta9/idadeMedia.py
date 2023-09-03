#Elabore um algoritmo para calcular a média de idade de um número indeterminado de pessoas. 
#O programa deve encerrar quando a idade digitada for 0. Ao encerrar o programa deve mostrar quantas leituras foram realizadas.
leituras = 0
idadetotal = 0

while True:
    idade = int(input("Digite sua idade: "))
    leituras += 1
    idadetotal += idade
    if idade == 0:
        media = idadetotal / leituras
        print(media)
        print(leituras)
        print("Programa encerrado")
        break