#FUP para ler dois valores: NUM1 e NUM2, e se NUM1 for maior que NUM2 executa a soma de NUM1 e NUM2; 
# caso contrário, executa uma subtração
print("Exercicio 7")
num1 = float(input("Digite um primeiro numero: "))
num2 = float(input("Digite um  segundo numero: "))
soma=num1+num2
sub=num1-num2
if num1 > num2:
   print(f"A soma dos numeros deu:  {soma}")
else:
    print (f"A subtracao dos numeros deu {sub}")
   