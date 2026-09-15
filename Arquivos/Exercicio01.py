from random import randint

# Bloco de leitura de arquivo
with open('Clientes.txt', 'r') as Clientes: # Podemos adicionar um encoding='utf-8' para permitir acentos
    
    prazo = 12
    
    for linha in Clientes:
        linha = linha.strip()
        if linha == '':
            continue # Se houver uma linha vazia, tente procurar um valor na próxima
        nome, valor = linha.split(';')
        
        clientes = {}
        print()
        
        i = randint(1, 4) / 100 # Transforma o int em porcentagem (para fazer a conta corretamente) (está dentro do for para gerar um juros diferente para cada um)
        
        pmt = float(valor) * ((i * ((i + 1) ** prazo)) / (((i + 1) ** prazo) - 1))
        
        print(f'O Cliente: {nome} pretende financiar o valor de R${valor}')
        print(f'O valor do juros é de {i*100:.1f}%, cada parcela paga será de: R${pmt:.2f}') # i * 100 para formatar o juros e passar o valor correto
        
        # Criando um dicionário com os valores
        
        clientes['Nome'] = nome
        clientes['Financiamento'] = valor
        clientes['Juros'] = (f'{i * 100:.1f}')
        clientes['Vl Parcela'] = (f'{pmt:.2f}')
        
        print(clientes)