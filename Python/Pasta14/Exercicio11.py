for i in range(10):
    nota01=float(input('Digite a nota 1: '))
    nota02=float(input('Digite a nota 2: '))
    nota03=float(input('Digite a nota 3: '))
    media= (nota01+nota02+nota03)/3
    if media>=7:
        print('Aprovado')
    else:
         print('Reprovado')