#Escrever um programa que lê o número de um funcionário, o número de horas por ele trabalhadas, 
# o valor que recebe por hora, o número de filhos com idade inferior a 14 anos, a idade, o tempo de serviço do funcionário e 
# um valor fixo de salário família por filho. Calcular o salário bruto, o desconto do INSS (8,5% do salário bruto) e o salário família total. 
# Calcular o IR (Imposto de Renda) como segue: 

#Se SB > 1.500,00 então IR = 15% do SB
#Se SB > 500,00 e SB <= 1.500,00 então IR = 8% do SB
#Se SB <= 500,00 então IR = 0.
#Escrever o número do funcionário, salário bruto, total dos descontos, e salário líquido.

print("Exercicio 2")

NFuncionario= int(input("Digite o numero do funcionario: " ))
HFuncionario= float(input("Digite o numero de horas trabalhadas: "))
VHFuncionario= float(input("Digite o salario por hora: "))
FFuncionario= float(input("Digite o numero de filhos acima de 14 anos do funcionario:  "))
IFuncionario= float(input("Digite a idade do funcionario: "))
TFuncionario= float(input("Digite o tempo de serviço do funcionario: "))
VFFuncionario= float(input("Digite um valor fixo de salário família por filho:  "))
FormulaSB= (HFuncionario * VHFuncionario) + (VFFuncionario * FFuncionario)
DescontoINSS= (FormulaSB * 0.85)

if FormulaSB > 1.500:
  salarioLiquido= DescontoINSS - (FormulaSB * 0.15)
  print(f"O funcionario de numero {NFuncionario} ficou com um salario bruto de R${FormulaSB}, com desconto ficou R${DescontoINSS} e seu salario liquido ficou R${salarioLiquido}")
 
elif FormulaSB > 500  <= 1.500:
  salarioLiquido= DescontoINSS - (FormulaSB / 100 * 0.08)
  print(f"O funcionario de numero {NFuncionario} ficou com um salario bruto de R${FormulaSB}, com desconto ficou R${DescontoINSS} e seu salario liquido ficou R${salarioLiquido}")
 
elif FormulaSB <= 500:
 salarioLiquido= DescontoINSS - (FormulaSB / 100 * 0)
 print(f"O funcionario de numero {NFuncionario} ficou com um salario bruto de R${FormulaSB}, com desconto ficou R${DescontoINSS} e seu salario liquido ficou R${salarioLiquido}")


