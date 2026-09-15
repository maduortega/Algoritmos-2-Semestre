# Função para a atualizar o estoque
def atualizar(estoque: dict, movimentacao: list):
    for mov in movimentacao:
        produto = mov[0]
        qtd = mov[1]
        
        if produto not in estoque:
            estoque[produto] = {'Saldo': qtd, 'Min': 0, 'Preço': 0}
        
        estoque[produto]['Saldo'] += qtd

def listar(estoque):
    #saldo = produto.get('Saldo')
    #minimo = produto.get('Min')
    for produto in estoque:
        if produto.get('Saldo') < produto.get('Min'):
            print(produto.get('Chave'))
                
# Função main
def main():
    estoque = {
        "café": {"Saldo": 10, "Min": 12, "Preço": 12.50},
        "pão": {"Saldo": 30, "Min": 25, "Preço": 2.00},
        "queijo": {"Saldo": 5, "Min": 12, "Preço": 34.00},
    }

    movimentacao = [
        ["café", -3],
        ["pão", -10],
        ["café", 5],
        ["leite", 8] # produto novo não cadastrado
    ]
    
    # Atualizar o estoque a partir das movimentações diárias
    atualizar(estoque, movimentacao)
    
    # Listar quais produtos ficaram abaixo do mínimo
    listar(estoque)

# Programa principal
if __name__ == '__main__':
    main()