nomeDoFuncionario=input('Digite o Nome: ')
salario=float(input('Qual o salário atual do funcionário?'))
correcao=0
 
if salario >= 400:
   correcao=0.15
elif salario > 400 and salario <= 700:
    correcao= 0.12
elif salario > 700 and salario <= 1000:
    correcao = 0.10
elif salario > 1000 and salario <= 1800:
    correcao = 0.07
elif salario > 1800 and salario <= 2500:
    correcao = 0.04
else:correcao = 0
 
salarioCorrigido= salario + (correcao * salario)
 
print(f'{nomeDoFuncionario} seu salário atual é de: R${salario} e obteve uma correção de: {correcao}x tornando seu salário para: {salarioCorrigido}')
