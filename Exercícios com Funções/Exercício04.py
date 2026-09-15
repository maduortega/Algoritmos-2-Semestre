# Função para verificar se um número é primo
from math import sqrt
'''Exercício incompleto'''
def eh_primo(valor: int) -> bool: # Bool = boleano, True or False!
    n_divisores = 0
    for i in range(2, sqrt(valor)):
        if valor % i == 0:
            n_divisores += 1
    if n_divisores == 2:
        valor += i
        
# Função para gerar n números primos dentro de uma lista

def gerar_primos(n: int) -> list:
    lista = []
    valor = 2
    while len(lista) <= n: # Len(lista) - tamanho da lista
        if eh_primo(valor):
            lista.append(valor)
        valor += 1
    return lista

# Função Main

def main(): # Em geral ela não retorna um valor, então não é preciso colocar None
    n = int(input('Informe uma quantidade de números primos: '))
    lista = gerar_primos(n)
   # imprimir(lista)

# Programa principal

if __name__ == '__main__':
    main()