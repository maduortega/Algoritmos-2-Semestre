from Professor import Professor

lista = []
qtd = int(input('Informe a quantidade de professores: '))

for _ in range(qtd):
    nome = input('Informe o nome do(a) professor(a): ')
    n_aulas = int(input('Informe seu número de aulas semanais: '))
    hr_aula = float(input('Informe o valor da hora aula: '))
    titulo = input('Informe seu título = mestre / doutor / outro: ')
    hr_extra = input('Informe se foi feito horas extras = sim / nao: ')
    
    lista.append(Professor(nome, n_aulas, hr_aula, titulo, hr_extra))

print('-' * 40)

for prof in lista:
    print(f'O salário bruto do(a) professor(a): {prof.nome} é: {prof.salario_bruto()}')