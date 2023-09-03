#A clínica PicaPau de hemodiálise realiza acompanhamento e tratamento de 110 pacientes renais crônicos de várias cidades do litoral norte do RS. 
# Os pacientes realizam sessões de hemodiálise 3 vezes na semana, sendo que, cada sessão dura entre 2 a 4 horas conforme a 
# diferença entre o peso seco e o peso atual.

#Faça um programa para calcular o peso seco de um paciente que está realizando hemodiálise. E o tempo que ele irá ficar em sessão de hemodiálise.

#Considere o peso seco: o resultado do seu balanço hídrico, ou seja, o peso sem edema, 
# descontando os valores de líquidos ingeridos deste paciente em 24h. Utilize a seguinte fórmula: 
# peso seco = Peso atual - quantidade de  líquidos ingeridos nas últimas 24 h.

#Mostre a diferença entre esses valores: peso seco e peso atual para calcular o tempo de
#sessão de cada paciente e mostre quanto tempo pode ser a sessão de hemodiálise conforme a tabela.

#Diferenca_Peso >1 e <2 2h
#Diferenca_Peso  >2 e <3 3h
#Diferenca_Peso  >3 4h

pesoAtual=float(input("Digite seu peso atual: "))
liquido= float(input('Digite a quantidade de liquidos ingeridos nas ultimas 24h em liquidos: '))
pesoSeco= pesoAtual - liquido
diferenca= pesoAtual - pesoSeco

if diferenca >=1 and diferenca <2: 
    print(f'Sessao de 2h')
elif diferenca >=2 and diferenca <=3:
    print(f'Sessao de 3h')
elif diferenca >=3.1:
    print(f'Sessao de 4h')

print(f'A diferença do peso atual e do peso seco é {diferenca}, por isso seria este o horario da sessao.')