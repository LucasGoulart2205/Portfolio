#Faça um algoritmo (FUA) que lê o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. 
#O algoritmo deve calcular e mostrar o salário deste funcionário.

print('Exercicio 5')

funcionarios= input('Digite o nome do funcionario:')
horas= float(input('Digite o seu numero de horas trabalhadas:'))
valor_por_hora= float(input('Digite o valor recebido por hora:'))
salario= (horas*valor_por_hora)

print(f'{funcionarios} recebe um total de R$:{salario}')