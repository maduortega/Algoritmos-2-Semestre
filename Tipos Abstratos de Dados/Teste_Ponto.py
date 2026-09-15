from Ponto import Ponto

lista = []
qtd = int(input('Qual a quantidade de pontos? '))

for i in range(qtd):
    x = float(input('Coordenada x: '))
    y = float(input('Coordenada y: '))
    
    lista.append(Ponto(x, y))
    
print('-' * 40)

# Impressão de cada ponto e sua respectiva distância até o centro
print(f'Distância de cada ponto até a origem (0,0):')
for pontos in lista:
    print(f'{pontos} --> {pontos.dist_origem()}')
    
print('-' * 40)
print(f'Distância entre os pontos 1 e 2')
print(lista[0].calcular_dist(lista[1])) # Passamos o índice 1 como o outro ponto (p) | lista[0] é o self