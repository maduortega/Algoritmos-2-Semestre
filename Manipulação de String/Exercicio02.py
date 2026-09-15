import random

# Função para jogar
def jogar(palavras: str) -> str:
    # segredo2 = palavras[random.randint(0, len(palavras))] versão pra escolher pelo número
    segredo = random.choice(palavras).lower()
    
    # Listas auxiliares
    underline = ['_'] * len(segredo)
    
    erro = 0
    
    while erro <= 6 and '_' in underline: # Enquanto tiver _ dentro da lista underline
        print(f'{underline}')
        letra = input('Chute uma letra: ')
        
        if letra in segredo:
            for i in range(len(segredo)): # Tamanho da palavra que está em segredo
                if segredo[i] == letra:
                    underline[i] = letra
        else:
            erro += 1
            print(f'Você errou pela {erro}ª vez, tente novamente.')
    
    if '_' not in underline:
        print(f'Você acertou! {underline}')
    else:
        print('Você foi enforcado ☠')

# Função para ler e armazenar as palavras
def ler_palavras() -> str:
    palavras = []
    for i in range(5):
        palavras.append(input('Informe uma palavra: '))
    return palavras

# Função Principal
def main():
    palavras = ler_palavras()
    jogar(palavras)

# Programa Principal
if __name__ == '__main__':
    main()