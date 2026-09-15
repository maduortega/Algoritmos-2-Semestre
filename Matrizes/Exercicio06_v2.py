from random import randint

def ler_dados(matriz):
    matriz = [[randint(1, 5) for j in range(len(matriz[i]))] for i in range(len(matriz))]
    
def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='\t')
        print()

def multiplicar(a, b):
    c = []
    for i in range(len(a)):
        linha = []
        for j in range(len(b[0])): # i pega a linha da matriz A, não podemos usá-lo,
            aux = 0                   # o 0 pega o tamanho da linha 0 (total de colunas)
            for k in range(len(a[i])):
                aux += a[i][k] * b[k][j]
            linha.append(aux)
        c.append(linha)
    return c
      
# Programa principal
a = [[1, 2], [3, 0], [2, 1]]
b = [[1, 0, 1], [2, 1, 3]]

print('Matriz A')
imprimir(a)
print()

print('Matriz B')
imprimir(b)

c = multiplicar(a, b)
print()
print('Matriz C')
imprimir(c)