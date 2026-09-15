# Função recursiva para calcular o fatorial de um número inteiro e positivo
def fatorial(n: int) -> int:
    # Caso base
    if n == 0:
        return 1
    return n * fatorial(n-1)

# Função principal
def main():
    n = int(input('Informe um número inteiro e positivo:'))
    if n < 0:
        print('INTEIRO E POSITIVO 😠')
    else:
        print(f'{n}! = {fatorial(n)}')
    
# Programa principal
if __name__ == '__main__':
    main()