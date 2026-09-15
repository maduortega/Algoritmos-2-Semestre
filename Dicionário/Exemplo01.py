# Progama exemplo para ler o RA, o nome e a nota dos alunos de determinada disciplina
# Em seguida imprimir a quantidade de alunos com média >= 7

lista = []

for i in range(5):
    ra = int(input('RA: '))
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    lista.append({'RA': ra, 'Nome': nome, 'Nota': nota })
    print()

# Quantidade de alunos que estão com nota acima da média
total = 0
for aluno in lista:
    if aluno.get('nota') >= 7.0: # busca o valor associado a chave nota (>= 7 passam)
        total += 1

print(total)