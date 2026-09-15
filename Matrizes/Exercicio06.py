from random import randint

# Função para gerar a matriz com valores aleatórios
def gerar_matrizes():
    m1 = [[randint(0, 10) for j in range(2)] for i in range(3)]
    m2 = [[randint(0, 10) for j in range(3)] for i in range(2)]
    
    return m1, m2

# Função para imprimir a matriz no terminal
def imprimir_matrizes(m1, m2):
    print('Matriz 3x2')
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            print(m1[i][j], end='\t')
        print()
    print()

    print('Matriz 2x3')
    for i in range(len(m2)):
        for j in range(len(m2[i])):
            print(m2[i][j], end='\t')
        print()
    print()

def multiplicar(m1, m2):
    m3 = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m2[0])):
            aux = 0
            for k in range(len(m1[i])):
                aux += m1[i][k] * m2[k][j]
            linha.append(aux)
        m3.append(linha)
    return m3

def imprimir_multiplicacao(m3):
    print('Matriz final')
    for i in range(len(m3)):
        for j in range(len(m3[i])):
            print(m3[i][j], end='\t')
        print()
    print()

# Função Main
def main():
    
    m1, m2 = gerar_matrizes()
    imprimir_matrizes(m1, m2)
    m3 = multiplicar(m1, m2)
    imprimir_multiplicacao(m3)
    
# Programa principal
if __name__ == '__main__':
    main()