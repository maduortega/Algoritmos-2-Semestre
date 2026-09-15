# Variável global
num_calls = 0

def fib(n: int) -> int:
# Caso base
    global num_calls
    if n == 0:
        return 0
    elif n == 1: # não preicsamos do n == 2, pois, a partir do 2° número já podemos somar os anteriores (0, 1)
        return 1
    num_calls += 2 # += 2 pois a função está sendo chamada duas vezes (fib(n - 1)) e (fib(n - 2))
    return fib(n - 1) + fib(n - 2)

qtd = int(input())
for i in range(qtd):
    n = int(input())
    num_calls = 0 # Zerando a chamada depois de rodar a função (se não ele vai ir somando)
    f = fib(n)
    print(f'fib({n}) = {num_calls} calls = {fib(n)}')