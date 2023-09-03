TotalIdade=0


for i in range(0,10):
    idade=int(input("Digite sua idade: "))
    peso=float(input("Digite seu peso: "))
    altura=float(input("Digite sua altura: "))
    TotalIdade= idade + TotalIdade
    
mediaIdade= int(TotalIdade / 3)
print(f"A media das idade é de {mediaIdade} anos.")
pessoasSegundaPergunta=0


if peso > 90 and altura < 1.50:
     pessoasSegundaPergunta += 1

print(f"Quantidade de pessoas com peso acima de 90kg e altura inferior a 1.50m: {pessoasSegundaPergunta}.")   

pessoasTerceiraPergunta=0
if idade > 10 and idade <30 and altura > 1.90:
    pessoasTerceiraPergunta += 1

porcentagem=(pessoasTerceiraPergunta * 3 / 100)

print(f"A porcentagem de pessoas maior que 10 e inferior a 30 anos com altura maior que 1.90 é de {porcentagem} ")

   
