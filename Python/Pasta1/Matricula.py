# FUP que le o nome do estudante, numero da matricula, o email institucional, e quantas cadeira o estudante faz, 
# e mostre quanto de desconto ele recebera caso va em algum cinema sabendo que o valor da ingresso pro cinema é R$30:
#
#    Inferior igual a tres cadeiras 15%;
#    Superior igual a quatro cadeiras 35%;

NomeEstudante=input("Digite Seu Nome Completo: ")
NumeroMatricula=int(input("Digite Seu Numero de Matricula: "))
EmailEstudante=input("Digite Seu Email Institucional : ")
CadeirasEstudante=int(input("Digite Quantas Cadeiras voce esta fazendo: "))

if CadeirasEstudante <= 3 :
    print(f"{NomeEstudante} Voce recebera 15% de desconto caso for em algum cinema. ")

elif CadeirasEstudante >= 4 :
    print(f"{NomeEstudante} Voce recebera 35% de desconto caso for em algum cinema. ")