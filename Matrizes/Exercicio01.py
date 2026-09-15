# Apenas Vetor

from random import randint

lista_original = []
lista_nova = []

# Lendo os valores para a lista original
for i in range(5):
    lista_original.append(randint(1,10))
    if lista_original[i] not in lista_nova:
        lista_nova.append(lista_original[i])
    
print(lista_original)
print(lista_nova)