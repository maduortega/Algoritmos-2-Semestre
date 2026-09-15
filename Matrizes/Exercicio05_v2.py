from random import randint

# Função para gerar a matriz com valores aleatórios
def gerar_matriz():
    ordem = randint(2, 5) # Gera um tamanho aleatório para matriz (quadrada)
    matriz = [[randint(1, 10) for j in range(ordem)] for i in range(ordem)]
    return matriz

# Função para imprimir a matriz no terminal
def imprimir(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end='\t')
        print()

def trocar(matriz):
    j = len(matriz) - 1
    for i in range(len(matriz)):
        aux = matriz[i][i]
        matriz[i][i] = matriz[i][j]
        matriz[i][j] = aux
        j -= 1

def main():
    
# Preenchendo a matriz
    matriz = gerar_matriz()
    
    print('Impressão antes da troca')
    imprimir(matriz)
    
    trocar(matriz)
    print()
    
    print('Impressão pós troca')
    imprimir(matriz)
    
# Programa principal
if __name__ == '__main__':
    main()