# Função para retornar a multiplicação entre dois números sem usar o *
def multiplicar(m: int, n: int) -> int:
    if n == 0:
        return n
    if n > 0:
        return m + multiplicar(m, n - 1) # Para números positivos (Mas se o M for negativo, funciona)
    return -multiplicar(m, -n)        # Para números negativos (Agora se o N for negativo, funciona)

# Função principal
def main():
    m = int(input('Informe o primeiro valor: '))
    n = int(input('Informe o segundo valor: '))
    print(f'{m} * {n} = {multiplicar(m, n)}')
    

# Programa principal
if __name__ == '__main__':
    main()