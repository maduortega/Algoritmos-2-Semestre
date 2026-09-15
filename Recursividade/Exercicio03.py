# Função MDC para calcular e retornar o máximo divisor comum
def mdc(m: int, n: int) -> int:
    if n > m:
        return mdc(n,m)
    elif n == 0:
        return m
    return mdc(n, (m % n))            # Não precisa colocar else, mas poderia

# Função principal
def main():
    m = int(input('Informe o primeiro valor: '))
    n = int(input('Informe o segundo valor: '))
    print(f'mdc({m}, {n}) = {mdc(m, n)}')

# Programa principal
if __name__ == '__main__':
    main()