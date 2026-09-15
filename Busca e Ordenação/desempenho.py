from random import randint
import time
import Util

def medir_tempo(algoritmo, lista: list) -> float:
    lista_aux = lista.copy() # Copia da lista
    inicio = time.perf_counter() # Relógio mais eficiênte do python para simulação
    algoritmo(lista_aux) # Quando o algoritmo chamar o Bolha, ele vai estar fazendo referência para o bolha
    fim = time.perf_counter()
    
    return (fim - inicio) * 1000 # Para ficar em milissegundos (* 1000)

def gerar_lista(n: int) -> list:
    lista = []

    for _ in range(n):
        lista.append(randint(1, n ** 2)) # Gera de 1 até n ao quadrado (se for 10, vai gerar até 100)
    return lista

def main():
    tamanho = [100, 1000, 10000]
    print(f'Comparação entre os métodos de ordenação')
    print()
    
    for n in tamanho:
        print(f'Lista de tamanho {n}:')
        lista = gerar_lista(n)
        
        tempo_bolha = medir_tempo(Util.bolha, lista) # O nome da função está sendo passado como parâmetro
        tempo_selecao = medir_tempo(Util.selecao, lista)
        tempo_insercao = medir_tempo(Util.insercao, lista)
        tempo_quicksort = medir_tempo(Util.quicksort, lista)
        tempo_mergesort = medir_tempo(Util.mergesort, lista)
        
        print(f'Tempo bolha {tempo_bolha:.3f}')
        print(f'Tempo seleção {tempo_selecao:.3f}')
        print(f'Tempo inserção {tempo_insercao:.3f}')
        print(f'Tempo quicksort {tempo_quicksort:.3f}')
        print(f'Tempo mergesort {tempo_mergesort:.3f}')
        print('-' * 40) # Esse traço vai se repetir 40 vezes

if __name__ == '__main__':
    main()