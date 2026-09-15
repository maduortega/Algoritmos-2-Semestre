# Função recursiva que calcula o valor de um número elevado a alguma potência
def potencia(x: int, n: int) -> int:
    # Caso base
    if n == 0:
        return 1
    return x * potencia(x, n - 1)

# Função principal
def main():
    x = int(input('Indique um número base, positivo e inteiro: '))
    n = int(input('Informe uma potência para esse número, que seja inteira e positiva: '))
    if n <= 0 or x <= 0:
        print('Inteiro, positivo e diferente de 0')
    else:
        print(f'{x}^{n} = {potencia(x, n)}')
    
# Programa principal
if __name__ == '__main__':
    main()