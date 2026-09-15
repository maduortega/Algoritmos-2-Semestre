from random import randint
from math import sqrt

# Função para gerar a lista de pontos        
def gerar_pontos():
    lista = [] # --> lista = list()
    
    for _ in range(randint(1, 5)):
        lista.append((randint(-10, 10), randint(-10, 10))) # ou duas variáveis cada uma com um valor (x, y) e depois colocamos numa tupla (t = x, y)
    return lista                                        # talvez seja preciso uma tupla vazia antes (t = ()) ou colocariamos a, b no append da lista

# Função para calcular a distância de cada um dos pontos até a origem
def calcular(lista):
    distancia = []
    
    for i in range(len(lista)): # ou i in lista (ai só usamos o i sem lista[i])
      x, y = lista[i] # Desempacotando
      distancia.append(sqrt(x * x + y * y))
    return distancia

# Função para achar o ponto mais distante da origem
def achar_maior(lista, distancia):
    ponto = lista[0] # pega o elemento no índice 0 da lista
    maior = distancia[0]
    
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

# Função para achar o ponto menos distante da origem
def achar_menor(lista, distancia):
    ponto = lista[0] # pega o elemento no índice 0 da lista
    maior = distancia[0]
    
    for i in range(len(lista)):
        if distancia[i] < maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

# Função para calcular a média das distâncias
def media(distancia):
    soma = 0
    
    for d in distancia: # Pega o elemento dentro da lista de distância
        soma += d # Guarda o valor dentro da distância e soma na variável soma
    
    return soma / len(distancia)

# Função main
def main():
    
    lista = gerar_pontos()
    distancia = calcular(lista)
    
    for i in range(len(lista)):
        print(f'Coordenada: {lista[i]} --> Distância: {distancia[i]: .2f}')
    print()
    
    print(f'Ponto mais distante em relação a origem --> {achar_maior(lista, distancia)}')
    print(f'Ponto menos distante em relação a origem --> {achar_menor(lista, distancia)}')
    print(f'Média das distâncias --> {media(distancia): .2f}')

# Programação principal
if __name__ == '__main__':
    main()