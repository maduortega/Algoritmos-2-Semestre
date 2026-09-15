a = input('Informe uma palavra: ').lower() # Todas as letras informadas serão minúsculas
for letra in a:
    print(f'letra = {letra} | código = {ord(letra)}') # Ord de ordinal
                                                      #  Pega a ordem, a posição daquele caractere

lista = [4, 6, 97, 124] # Transformando números em caracteres

for i in lista: # Desta maneira ele controla a lista toda (sem o range)
    print(chr(i)) # Str mudaria apenas o TIPO do número, assim ele converte da forma certa