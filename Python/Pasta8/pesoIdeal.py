#1. Faça um programa que leia a altura e o sexo de uma pessoa, calcule seu peso ideal, 
# utilizando as seguintes fórmulas:

#para homens : (72.7*altura) –58;

#para mulheres : (62.1*altura) – 44.7.


print('Exercicio 1')

altura= float(input('Digite sua altura:'))
sexo= (input('Digite seu sexo:'))
CalculoHomem= ((72.7*altura) -58)
CalculoMulher= ((62.1*altura) -44.7)

if (sexo == "Masculino"):
    CalculoHomem= ((72.7*altura) -58)
    print(f'O seu peso Ideal deve ser {CalculoHomem}')

else: 
    CalculoMulher= ((62.1*altura) -44.7)
    print(f'O seu peso Ideal deve ser {CalculoMulher}')


