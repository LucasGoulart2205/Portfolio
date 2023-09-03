#Elabore um algoritmo para calcular a média de idade de um número indeterminado de pessoas. 
#O programa deve encerrar quando a idade digitada for 0.
# Ao encerrar o programa deve mostrar quantas leituras foram realizadas.
media=0
todasIdades=0
leituras=0
idades=0
while True:
    idades=int(input("Digite sua idade: "))
    todasIdades += idades
    media +=1
    mediaIdades= (todasIdades / media)
    leituras=leituras + 1
    print(leituras)
    if  idades != 0 :
        print(mediaIdades)
    else:
        print(f"{leituras} pessoas digitaram ")
        break