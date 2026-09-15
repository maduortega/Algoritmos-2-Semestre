# Função para imprimir os valores

def imprimir(n: int) -> None:
    while True:
        print(f'{n}', end=' ') # Espaço dentro do ' ' para os números não imprimirem colados
        if n == 1:
            break
        elif n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2 # Duas barras para uma divisão inteira, sem casas decimais

# Função principal (main)

def main() -> None:
    n = int(input('Informe um número: '))
    imprimir(n)
    
# Programa principal

if __name__ == '__main__':
    main()