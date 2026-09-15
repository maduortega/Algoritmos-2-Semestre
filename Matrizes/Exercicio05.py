from random import randint

# Preenchendo a matriz
matriz = [[randint(1, 10) for j in range(3)] for i in range(3)]

# Imprimindo a matriz com formato de matriz
print('Matriz antiga')

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end='\t')
    print()

# Trocando os elementos da dp com a ds (e vice-versa)
j = len(matriz) - 1
for i in range(len(matriz)):
    aux = matriz[i][i]
    matriz[i][i] = matriz[i][j]
    matriz[i][j] = aux
    j -= 1

# Matriz nova com formato de matriz e com dp e ds invertidas
print()
print('Matriz nova')

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end='\t')
    print()