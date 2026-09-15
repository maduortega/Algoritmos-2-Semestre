import random

# Função para saber se há saída do labirinto
def encontrar_caminho(labirinto, atual, saida, coordenadas_verificadas):
    
    if atual == saida:
        return True
    
    x, y = atual
    
    caracteres_possiveis = ["S", "."]
    coordenadas_verificadas.append(atual)
    
    # CIMA
    if x > 0:
        if labirinto[x - 1][y] in caracteres_possiveis and (x - 1, y) not in coordenadas_verificadas:
            if encontrar_caminho(labirinto, (x - 1, y), saida, coordenadas_verificadas):
                return True
    
    # DIREITA
    if y < len(labirinto) - 1:
        if labirinto[x][y + 1] in caracteres_possiveis and (x, y + 1) not in coordenadas_verificadas:
            if encontrar_caminho(labirinto, (x, y + 1), saida, coordenadas_verificadas):
                return True
            
    # BAIXO
    if x < len(labirinto) - 1:
        if labirinto[x + 1][y] in caracteres_possiveis and (x + 1, y) not in coordenadas_verificadas:
            if encontrar_caminho(labirinto, (x + 1, y), saida, coordenadas_verificadas):
                return True
            
    # ESQUERDA
    if y > 0:
        if labirinto[x][y - 1] in caracteres_possiveis and (x, y - 1) not in coordenadas_verificadas:
            if encontrar_caminho(labirinto, (x, y - 1), saida, coordenadas_verificadas):
                return True
            
    return False
            

# Função para imprimir o labirinto
def imprimir_labirinto(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto)):
            print(labirinto[i][j], end='\t')
        print()

# Função que gera o labirinto
def gerar_labirinto(ordem, caracteres):
    labirinto = [[random.choice(caracteres) for j in range(ordem)] for i in range(ordem)]
    while True:
        inicio_X = random.randint(0, ordem - 1)
        inicio_Y = random.randint(0, ordem - 1)
        fim_X = random.randint(0, ordem - 1)
        fim_Y = random.randint(0, ordem - 1)
        if inicio_X != fim_X or inicio_Y != fim_Y:
            labirinto[inicio_X][inicio_Y] = "E"
            labirinto[fim_X][fim_Y] = "S"
            break  
    return labirinto, (inicio_X, inicio_Y), (fim_X, fim_Y)

# Função principal
def main():
    ordem = int(input("Qual a ordem da matriz: "))
    caracteres = ["#", "."]
    labirinto, coordenada_E, coordenada_S = gerar_labirinto(ordem, caracteres)
    imprimir_labirinto(labirinto)
    coordenadas_verificadas = []
    existe_caminho = encontrar_caminho(labirinto, coordenada_E, coordenada_S, coordenadas_verificadas)
    print(existe_caminho)

# Programa principal
if __name__ == "__main__":
    main()
