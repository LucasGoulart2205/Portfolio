print("Menu de opções \n 1-Média Aritmetica \n 2-Média Ponderada \n 3-Sair \n ")

opcoes=int(input("Escolha uma opção: \n"))

if opcoes <= 1:
    number1=int(input("Digite um numero:\n"))
    number2=int(input("Digite um numero:\n"))
    
    mediaAritmetica= (number1 + number2) / 2

    print(f"A média Aritmetica é : {mediaAritmetica}.")

numerador=0
denominador=0

if opcoes >=2 and opcoes < 3:
    for i in range (3):
            nota = float(input("Digite uma nota:\n"))
            peso = float(input("Digite um peso:\n"))
            
            numerador = numerador + nota*peso
            denominador = denominador + peso
    result=(numerador / denominador)
    print (f"A Média Ponderada é: {result}")

if opcoes >=3: 
    print (f"Saindo do Menu...")