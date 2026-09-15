from random import randint

# Função para gerar a lista de tuplas      
def gerar_listas():
    lista = []
    
    for _ in range(randint(3, 3)):
        b = randint(0, 10)
        a = randint(0, b) # O B só pode ser <= A (ficou confuso mas, A <= B == B <= A)
        t = (a, b)
        lista.append((t))
    return lista

def sobrepor(lista):
    lista_nova = []
    t = ()
    aux_a, aux_b = lista[0] # Pega o primeiro valor da lista de tuplas como base de comparação
    
    for i in range(len(lista)):
        a, b = lista[i] # Vai percorrer todas as tuplas dentro da lista de tuplas
        if a < aux_b: # Se A estiver dentro do intervalo e B for maior que a auxiliar, substituimos
            if b > aux_b:
                aux_b = b
        if b < aux_b: # Se B estiver dentro do invervalo e A for menor que a auxiliar, substituimos
            if a < aux_a:
                aux_a = a
        t = (aux_a, aux_b)
    lista_nova.append(t)

    return lista_nova

# Função main
def main():
    lista = gerar_listas()
    print(lista)
    
    a = sobrepor(lista)
    print(a)

# Programação principal
if __name__ == '__main__':
    main()