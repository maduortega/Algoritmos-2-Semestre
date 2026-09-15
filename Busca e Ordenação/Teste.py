import Util
from random import randint

lista = [randint(1, 500) for _ in range(10)] # Preenche uma lista com 10 valores de 1 até 500
print(Util.ordenar(lista))