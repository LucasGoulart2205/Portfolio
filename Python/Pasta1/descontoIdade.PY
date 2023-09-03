# O Cinema de Torres está enfrentando problemas com descontos para as pessoas nas compras onlines, para isso ele precisa
# que voce FUP que pergunte o nome, idade e o sexo da pessoa, para que possa confirmar ao seu cliente que sua compra foi concluida. 
# Sabendo que tambem se a pessoa for >= 18 anos ele paga R$30 e se for < 18 paga meia entrada.

Nome=input("Digite Seu Nome Completo: ")
idade=int(input("Digite a idade:  "))
Sexo=input("Digite o sexo: ")

if idade >= 18:
     print(f'Parabéns {Nome}, seu cadastro foi concluido e a compra no valor de R$30,00 foi aprovada, bom filme!')

elif idade < 18:
    print(f'Parabéns {Nome}, seu cadastro foi concluido e a compra no valor de R$15,00 foi aprovada, bom filme!')