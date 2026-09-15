# Função para calcular o total de grãos
# Versão com laço de repetição

def contargraos():
    aux = 1  # O auxiliar fora do laço serve apenas para fornecer um primeiro valor
    for i in range(64):
        aux *= 2
    return aux
    
total = contargraos()
print(f'Total de grãos: {total}')

# Versão com potenciação

def contargraos2() -> int: # A seta informa que a função retorna um valor inteiro
    total = 0
    for i in range(64):
        total += 2 ** i
    return total

total2 = contargraos2()
print(f'Total de grãos: {total2}')

# Versão 

