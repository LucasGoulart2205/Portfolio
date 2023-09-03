#FUP que leia o número da conta bancária e o saldo de um cliente. 
# Caso a conta tenha saldo negativo, o programa deve enviar a seguinte mensagem: CONTA ESTOURADA, 
# caso contrário CONTA NORMAL.

print('Exercicio 10')

conta = float(input('Digite seu valor bancário: '))
 
if conta >= 0:
    print('Sua conta bancária está positiva.')
else:
    print('Sua conta esta negativa.')
