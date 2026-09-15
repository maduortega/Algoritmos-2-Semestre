p1 = [('Selmini', 8), ('Flávio', 7), ('Rafa', 9), ('Surian', 10)]
p2 = [('Selmini', 2), ('Flávio', 7), ('Rafa', 10), ('Surian', 10)]

melhor = []
pior = []
manteve = []

for i in range(len(p1)):
    aluno, nota1 = p1[i]
    aluno, nota2 = p2[i]
    diferenca = nota2 - nota1
    aux = (aluno, nota1, nota2, diferenca)
    if nota2 > nota1:
        melhor.append(aux)
    elif nota2 < nota1:
        pior.append(aux)
    else:
        manteve.append(aux)
        
print(f'Alunos que melhoraram sua nota --> {melhor}')
print(f'Alunos que pioraram sua nota --> {pior}')
print(f'Alunos que mantiveram sua nota --> {manteve}')