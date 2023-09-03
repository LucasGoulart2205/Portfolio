#FUP que le todos os  dados dos candidatos de um alistamento militar, como rg, cpf, nome completo,idade, 
# caso tenha problemas de saude dispense o candidato, caso contrario mostre que o canditato foi alistado corretamente

print("Alistamento Militar, Exercito Brasileiro")

rg=int(input("Digite seu RG :"))
cpf=int(input("Digite seu cpf: "))
nomeCandidato=(input(" Digite seu nome completo:"))
idade=int(input("Digite sua idade: "))
saude=(input("Voce possui algum problema grave de saude? Se sim digite S caso contrario digite N.  "))

if saude == "S":
    print(f"{nomeCandidato}Voce foi Selecionado para o Serviço Militar Obrigatório.")

else:
    print (f"{nomeCandidato}Voce foi dispensado do Serviço Militar Obrigatório. ")
