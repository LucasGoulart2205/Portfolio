
soma=0
nota=0
qnt=0
leituras=10

for qnt in range(10):
    nota=float(input('Digite a nota do aluno: '))
    soma=soma + nota 

media=soma/leituras
print(f'A media da é {media}')