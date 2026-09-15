# A partir de uma lista de palavras (que podem se repetir), imprimir a quantidade
# De vezes que cada palavra aparece, por último imprimir a ocorrência

# Entrada das palavras
lista = []
total = int(input('Qual o total de palavras? '))

for i in range(total):
    lista.append(input('Palavra: '))
print()

# Contar o número de ocorrências de cada uma cas palavras
ocorrencia_palavra = {}
for palavra in lista:
    if palavra in ocorrencia_palavra:
        ocorrencia_palavra[palavra] += 1 # Pega o valor associado a chave palavra
    else:
        ocorrencia_palavra[palavra] = 1
 
# Contar a ocorrência das letras       
ocorrencia_letras = {}
for palavra in lista:
    for letra in palavra:
        if letra in ocorrencia_letras:
            ocorrencia_letras[letra] += 1
        else:
            ocorrencia_letras[letra] = 1
    
# Impressão da ocorrência das palavras
print('Ocorrência das palavras')
for chave, valor in ocorrencia_palavra.items():
    print(f'{chave} --> {valor}')
print()
    
print('Ocorrência das letras')
for chave, valor in ocorrencia_letras.items():
    print(f'{chave} --> {valor}')