# Soma dos números que estão na diagonal de uma matriz (principal e secundaria)
from random import randint

# Preenchendo a matriz
linha = 4
coluna = 4
dp = 0
ds = 0

matriz = [[randint(1, 10) for j in range(coluna)] for i in range(linha)] # Ou range(4)

# printar a matriz no formato de uma matriz
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end='\t') # \t espaçamento igualitário
    print()

# Soma dos elementos da diagonal principal e da secundária
for i in range(len(matriz)):
    for j in range(len(matriz)): # Só é valido pois a matriz é quadrada
        
        # Verifica se o elemento está na dp
        if i == j:
            dp += matriz[i][j]
         
        # Verifica se o elemento está na ds
        if i + j == len(matriz) - 1: # Sempre -1 pq a contagem começa no 0
            ds += matriz[i][j]
         
print(f'Soma dos elementos da diagonal principal {dp}')
print(f'Soma dos elementos da diagonal secundária {ds}')