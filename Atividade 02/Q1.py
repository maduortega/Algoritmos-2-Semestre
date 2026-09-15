from random import randint

# Função para gerar matriz
def gerar_matriz(linhas, colunas):
    m = [[randint(1, 10) for j in range(colunas)] for i in range(linhas)]
    return m

# Função para imprimir matriz
def imprimir_matriz(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end='\t')
        print()
    print()
    print()
    
# Função para classificar o valor
def classificar_valor(m, i, j, valores_ao_redor, matriz_classificada):
    if m[i][j] > max(valores_ao_redor):
        matriz_classificada[i][j] = "P"
    elif m[i][j] < min(valores_ao_redor):
        matriz_classificada[i][j] = "V"
    else:
        matriz_classificada[i][j] = "N"
        
# Função para gerar a nova matriz
def gerar_nova_matriz(m, matriz_classificada):
    valores_ao_redor = []
    for i in range(len(m)):
        for j in range(len(m)):
            # Verifica se o valor está na borda da matriz
            if (i == 0) or (j == 0) or (i == len(m) - 1) or (j == len(m) - 1):
                # Verifica se está em um dos cantos da diagonal principal
                if i == j:
                    # Verifica se está no M[0][0]
                    if i == 0:
                        valores_ao_redor.append(m[i][j + 1])
                        valores_ao_redor.append(m[i + 1][j + 1])
                        valores_ao_redor.append(m[i + 1][j])
                        classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                    # É executado se o valor está no último elemento da matriz, ou seja,
                    # o último elemento da diagonal principal
                    else:
                        valores_ao_redor.append(m[i][j - 1])
                        valores_ao_redor.append(m[i - 1][j])
                        valores_ao_redor.append(m[i - 1][j - 1]) 
                        classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                # Verifica se está no canto inferior da diagonal secundária
                elif i - j == len(m) - 1:
                    valores_ao_redor.append(m[i - 1][j])
                    valores_ao_redor.append(m[i][j + 1])
                    valores_ao_redor.append(m[i - 1][j + 1])
                    classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                # Verifica se está no canto superior da diagonal secundária
                elif j - i == len(m) - 1:
                    valores_ao_redor.append(m[i + 1][j])
                    valores_ao_redor.append(m[i][j - 1])
                    valores_ao_redor.append(m[i + 1][j - 1])
                    classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                else:
                    # Verica se está na primeira linha, sem estar nos cantos
                    if i == 0:
                        valores_ao_redor.append(m[i][j - 1])
                        valores_ao_redor.append(m[i + 1][j - 1])
                        valores_ao_redor.append(m[i + 1][j])
                        valores_ao_redor.append(m[i + 1][j + 1])
                        valores_ao_redor.append(m[i][j + 1])
                        classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                    # Verifica se está na primeira coluna, sem estar nos cantos
                    elif j == 0:
                        valores_ao_redor.append(m[i - 1][j])
                        valores_ao_redor.append(m[i - 1][j + 1])
                        valores_ao_redor.append(m[i][j + 1])
                        valores_ao_redor.append(m[i + 1][j + 1])
                        valores_ao_redor.append(m[i + 1][j])
                        classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                    # Verifica se está na última linha, sem estar nos cantos
                    elif i == len(m) - 1:
                        valores_ao_redor.append(m[i][j - 1])
                        valores_ao_redor.append(m[i - 1][j - 1])
                        valores_ao_redor.append(m[i - 1][j])
                        valores_ao_redor.append(m[i - 1][j + 1])
                        valores_ao_redor.append(m[i][j + 1])
                        classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
                    # Verifica se está na última coluna, sem estar nos cantos
                    elif j == len(m) - 1:
                        valores_ao_redor.append(m[i - 1][j])
                        valores_ao_redor.append(m[i - 1][j - 1])
                        valores_ao_redor.append(m[i][j - 1])
                        valores_ao_redor.append(m[i + 1][j - 1])
                        valores_ao_redor.append(m[i + 1][j])   
                        classificar_valor(m, i, j, valores_ao_redor,matriz_classificada) 
            # Leva em consideração os valores que estão no meio da matriz
            else:
                valores_ao_redor.append(m[i - 1][j - 1])
                valores_ao_redor.append(m[i - 1][j])
                valores_ao_redor.append(m[i - 1][j + 1])   
                valores_ao_redor.append(m[i][j + 1])
                valores_ao_redor.append(m[i + 1][j + 1])
                valores_ao_redor.append(m[i + 1][j])
                valores_ao_redor.append(m[i + 1][j - 1])
                valores_ao_redor.append(m[i][j - 1])
                classificar_valor(m, i, j, valores_ao_redor,matriz_classificada)
            valores_ao_redor = []
    return matriz_classificada                

# Função main
def main():
    linhas = int(input("Quantas linhas terá a matriz: "))
    colunas = int(input("Quantas colunas terá a matriz: "))
    print()
    matriz_principal = gerar_matriz(linhas, colunas)
    imprimir_matriz(matriz_principal)
    matriz_classificada = [[0 for j in range(colunas)] for i in range(linhas)]
    nova_matriz = gerar_nova_matriz(matriz_principal, matriz_classificada)
    imprimir_matriz(nova_matriz)

# Programa principal
if __name__ == "__main__":
    main()
