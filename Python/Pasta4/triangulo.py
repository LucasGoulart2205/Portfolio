#Sabendo que triângulo é uma Figura geométrica de três lados onde cada um dos lados é menor que a soma dos outros dois. 
#Faça um algoritmo que receba três valores e verifique se eles podem ser os comprimentos dos lados de um triângulo. 
#Caso ele não forme um triângulo. Deve ser informado que as medidas não formam um triangulo e deve ser solicitado  ao usuário responder 
#se quer informar novos valores ou encerrar programa. 
#Quando esses valores formarem um triângulo deve ser exibido a área do triangulo e o perímetro além dos valores informados. 
#Considere que todos vão ser um triangulo reto. Após o programa deve perguntar se deseja efetuar um novo cálculo.
encerraPrograma={"N"}
while encerraPrograma != "N":
    
    LadoA=int(input("Digite o lado A DO TRIANGULO: "))
    LadoB=int(input("Digite o lado B DO TRIANGULO: "))
    LadoC=int(input("Digite o lado C DO TRIANGULO: "))
    AmaisB=(LadoA+LadoB)
    AmaisC=(LadoA+LadoC)
    BmaisC=(LadoB+LadoC)
    perimetro= LadoA+LadoB+LadoC
    area= LadoA*LadoB*LadoC

    if AmaisB > LadoC and AmaisC and LadoB and BmaisC > LadoA:
        print("Formam um triangulo!")
        print(f"O perimetro do triangulo é: {perimetro} e a area é: {area}.")
        encerraPrograma=input("Digite S para continuar o programa ou N para encerrar: ")
        if encerraPrograma == "S" or "s":
            print("Carregando...")
        elif encerraPrograma == "N":
            print("Programa encerrado")
            break
    
    else:
        print("As medidas nao formam um triangulo")
        encerraPrograma=input("Digite S para continuar o programa ou N para encerrar: ")
        if encerraPrograma == "S":
            print("Carregando...")
        elif encerraPrograma == "N":
            print("Programa encerrado")
            break