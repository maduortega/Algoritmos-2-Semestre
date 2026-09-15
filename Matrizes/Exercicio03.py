from random import randint

def gerar_matriz():
    total_ano = int(input('Informe a quantidade de anos: '))
    total_mes = int(input('Informe a quantidade de meses: '))
    
    matriz = [[randint(5, 40) for j in range(total_mes)] for i in range(total_ano)]
    return matriz

def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])): # [i] conta as colunas em determinada linha
            print(matriz[i][j], end='\t')     # (usar quando a matriz não for quadrada)
        print()

def media_ano(matriz):
    lista = []

    for i in range(len(matriz)):
        soma = 0
        media = 0
        for j in range(len(matriz[i])): # os laços passam por todos os elementos
            soma += matriz[i][j]
        media = soma / (len(matriz[i])) # Média = dividir pelo total de colunas (elementos)
        lista.append(media)
    
    return lista

def imprimir_media(lista):
    for i in range(len(lista)):
        print(f'Ano {i + 1} --> {lista[i]: .2f}')

def determinar_maior(media):
    aux = media[0]
    ano = 0
    for i in range(len(media)):
        if media[i] > aux:
            aux = media[i]
            ano = i
   
    return ano

def determinar_menor(media):
    aux = media[0]
    ano = 0
    for i in range(len(media)):
        if media[i] < aux:
            aux = media[i]
            ano = i
                  
    return ano

# Função main
def main():

    matriz = gerar_matriz()
    imprimir(matriz)
    
    media = media_ano(matriz)
    print()
    
    print('Média Anual')
    imprimir_media(media)
    print()
    
    ano_maior_media = determinar_maior(media)
    print(f'O ano com a maior média é: {(ano_maior_media + 1)}')
    print()
    
    ano_menor_media = determinar_menor(media)
    print(f'O ano com a menor média é: {(ano_menor_media + 1)}')

# Programa principal
if __name__ == '__main__':
    main()