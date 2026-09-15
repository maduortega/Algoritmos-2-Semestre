# Programa com função recursiva para ler um valor inteiro e positivo e retorne o
# valor de fibonacci na posição indicada | Fazer recursividade neste caso é RUIM

# Função recursiva para calcular o fibonacci
def fibonacci(n: int) -> int:
# Caso base
    if n == 1 or n == 2: # A posição 1 e a posição 2 são iguais a 1
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2) # Aqui usamos a definição do problema

# Função principal
def main():
    n = int(input('Indique uma posição na sequência de fibonacci (valor inteiro e positivo):'))
    if n <= 0:
        print('INTEIRO E POSITIVO 😠')
    else:
        print(f'A {n}° posição de fibonacci é {fibonacci(n)}')
    
# Programa principal
if __name__ == '__main__':
    main()