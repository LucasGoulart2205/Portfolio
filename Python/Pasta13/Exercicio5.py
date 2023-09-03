#FUP que leia o código de um aluno e suas três notas. 
# Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes, 3. 
# Mostre o código do aluno, suas três notas, a média calculada e a mensagem “ APROVADO” se a média for maior ou igual a 7 e “REPROVADO” 
# se a média for menor que 7.
 
notaUm=float(input("Qual a primeira  nota?"))
notaDois=float(input("Qual a segunda  nota?"))
notaTres=float(input("Qual a terceira  nota?"))
 
media= (notaUm * 4) + (notaDois * 3) + (notaDois * 3) / 10
 
if media>= 7:
    print('APROVADO')
else: print("REPROVADO")
