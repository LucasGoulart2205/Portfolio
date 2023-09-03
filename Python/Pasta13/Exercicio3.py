#O departamento que controla o índice de poluição do meio ambiente mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. 
# O índice de poluição aceitável varia de 0.05 até 0.25. Se o índice sobe para 0.3 as indústrias do primeiro grupo são intimadas a suspenderem 
# suas atividades, se o índice cresce para 0.4 as do primeiro e segundo grupo são intimadas a suspenderem suas atividades e se o índice atingir 0
# .5 todos os 3 grupos devem ser notificados a paralisarem suas atividades. FUP que lê o índice de poluição medido e emite a notificação adequada 
# aos diferentes grupos de empresas.

indice = float(input('Qual é o índice de poluição medido no momento?'))
 
if indice >= 0.3 and indice < 0.4:
    print(f'Por conta do indice {indice} de poulição, o primeiro grupo de empresas será intimada a suspender suas atividades. ')
elif indice >= 0.4 and indice < 0.5:
    print(f'Por conta do indice {indice} de poulição, o segundo grupo de empresas será intimada a suspender suas atividades. ')
elif indice >= 0.5:
        print(f'Por conta do indice {indice} de poulição, todos os grupos de empresas será intimada a suspender suas atividades. ')
else:
    print(f' O indice {indice} de poluição está aceitavel.')
