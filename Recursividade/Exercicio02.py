# Função recursiva
def somar(n: int) -> int:
    # Caso base
    if n == 0:
        return 0
    return n % 10 + somar(n // 10)

# Função principal
def main():
    n = int(input('Informe um número com dois digitos ou mais: '))
    if n <= 0:
        print('Inteiro, positivo e diferente de zero')
    elif n < 10:
        print('O número deve ter 2 ou mais dígitos')
    else:
        print(f'A soma dos dígitos de {n} é = {somar(n)}')

# Programa principal
if __name__ == '__main__':
    main()