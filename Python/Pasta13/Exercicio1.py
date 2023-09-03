#O hotel Pica-Pau cobra 50,00 Reais a diária e mais uma taxa de serviços. A taxa de serviços é de:
#1,50 por dia, se número de diárias <15
#1,00 por dia, se número de diárias =15
#0,50 por dia, se número de diárias >15
#FUP que lê o número de diárias e calcula o total a ser pago pelo cliente.

taxa = 50
diarias = int(input("Digite o numero de dias?"))
 
if diarias < 15:
    print(f'Foram {diarias} dias e o valor a ser pago pelo cliente será de: {diarias * 1.5 + 50}')
 
elif diarias == 15:
    print(f' Foram {diarias} dias e o valor a ser pago pelo cliente será de: {diarias * 1 + 50}')
 
elif diarias > 15:
    print(f'Foram {diarias} dias e o valor a ser pago pelo cliente será de: {diarias * 0.5 + 50}')
