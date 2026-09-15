linha = int(input('Informe o número de linhas: '))
coluna = int(input('Informe o número de colunas: '))

m = []

# Controle de linha
for i in range(linha):
    aux = []
    # Controle de coluna
    for j in range(coluna):
        aux.append(int(input('Valor: ')))
        
    m.append(aux)
    
print(m)