#Uma loja de animais precisa de um algoritmo para calcular os custos de criação de coelhos.
#O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10.
#O algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.

print('Exercicio 8')

numero_coelhos= int(input('Digite o numero de coelhos:'))
custo= (numero_coelhos * 0.70) / 18 + 10

print(f'O custo total da criaçao de {numero_coelhos} coelhos é:{custo}')
