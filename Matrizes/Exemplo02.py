linha = int(input('Informe o número de linhas: '))
coluna = int(input('Informe o número de colunas: '))

m = [[int(input('valor: ')) for j in range(coluna)] for i in range(linha)]
# no lugar do int, poderiamos ter um 0, serviria para o range da coluna ter o que preencher
# Ele preencheria toda a linha com zeros, com input ele preenche com o que o usuario pede

print(m)