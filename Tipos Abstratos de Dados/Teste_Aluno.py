from Aluno import Aluno # Arquivo Aluno, classe Aluno

# a = Aluno('Selminininho', 44, 8.0, 10.0) -> Estamos chamando o construtor
# O tipo da variável 'a' é aluno (assim como str, int, float...) | Retornaria um objeto do tipo aluno
# 'a' é a variável que referencia o objeto | O nome dessa função Aluno() é construtor

# Lista de alunos:
lista = []

for _ in range(3):
    nome = input('Nome: ')
    ra = int(input('RA: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append(Aluno(nome, ra, nota1, nota2)) # Geramos o objetos e o guardamos na lista | Chamamos o construtor
    print('-' * 30) # O append deve estar dentro do for, caso contrário, só pegaria o último valor
    

# Impressão do nome, da média e da situação
# Cabeçalho da tabela
print(f'{'Nome':<20} {'Média':<10} {'Situação'}') # <20 = a coluna pode ter no máximo 20 chr, faz com que fique alinhado
print('-' * 40)

for alunos in lista: # Não precisa ser alunos, pode ser qualquer coisa
    media = alunos.calcular_media() # Não aparece automaticamente, mas funciona | Usamos de exemplo, da para fazer direto
    print(f'{alunos.nome :<20} {media:<10.2f} {alunos.situacao()}')
