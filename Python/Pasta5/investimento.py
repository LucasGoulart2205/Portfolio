print("Agencia Bancaria")
codigoCliente=int(input("Digite Seu codigo: \n"))

print("Digite qual foi o seu investimento: \n Poupança = 1 \n Poupança plus = 2 \n Fundos de renda fixa = 3")
tipoInvestimento=int(input(""))

valorInvestido=float(input("Digite qual foi o valor investido: \n"))

if tipoInvestimento == 1: 
    poupança= (valorInvestido *1.5 / 100)
    totalInvestidoPoupança=(poupança + valorInvestido)
    print (f"Total do investimento foi de R$ {valorInvestido}, e o total de juros recebidos foi de R$ {poupança}. ")

if tipoInvestimento == 2: 
    poupançaPlus= (valorInvestido * 2 /100)
    totalInvestidoPoupançaPlus=(poupançaPlus + valorInvestido)
    print (f"Total do investimento foi de R$ {valorInvestido}, e o total de juros recebidos foi de R$ {poupançaPlus}. ")

if tipoInvestimento == 3:
    FundosDeRendaFixa= (valorInvestido * 4 / 100)
    totalInvestidoPoupançaFundosDeRendaFixa=(FundosDeRendaFixa + valorInvestido)
    print (f"Total do investimento foi de R$ {valorInvestido}, e o total de juros recebidos durante um mês foi de R$ {FundosDeRendaFixa}. ")



