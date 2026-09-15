from Retangulo import Retangulo
from Ponto import Ponto

from random import uniform
from random import randint

lista = []
qtd = randint(1, 10)

for _ in range(qtd):
    p = Ponto(randint(3, 15), randint(4, 16))
    
    largura = uniform(5.0, 10.0)
    altura = uniform(3.0, 12.0)
    
    lista.append(Retangulo(largura, altura, p))

print('-' * 80)

# Impressão dos dados (:<20 para alinhar, o último não precisa ter! E pq por algum motivo da erro)
for r in lista:
    print(f'Área = {r.area():<10} | Perímetro = {r.perimetro():<10} | Coordenada do centro = {r.coord_centro()}')