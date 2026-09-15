
# Função para gerar o relatório
def gerar_relatorio(totais_venda, faturamento_total, qtd_por_item, mais_vendido, mais_faturado, ticket_medio):
    relatorio = {
        "totais_venda": totais_venda,
        "faturamento total": faturamento_total,
        "qtd_por_item": qtd_por_item,
        "mais_vendido": mais_vendido,
        "mais_faturado": mais_faturado,
        "ticket médio": ticket_medio
    }
    return relatorio

# Função para encontrar o produto com maior faturamento individual
def produto_com_maior_faturamento(qtd_por_item, precos):
    produto_com_maior_faturamento = []
    maior_faturamento = 0
    for produto, qtd in qtd_por_item.items():
        if precos.get(produto) * qtd == maior_faturamento:
            produto_com_maior_faturamento.append(produto)
        if precos.get(produto) * qtd > maior_faturamento:
            produto_com_maior_faturamento = [produto]
            maior_faturamento = precos.get(produto) * qtd
    
    return produto_com_maior_faturamento

# Função para verificar qual é o produto mais vendido
def encontrar_produto_mais_vendido(qtd_por_item):
    produtos_mais_vendidos = []
    maior = 0
    for produto, valor in qtd_por_item.items():
        if valor == maior:
            produtos_mais_vendidos.append(produto)
        if valor > maior:
            produtos_mais_vendidos = [produto]
            maior = valor
    if maior == 0:
        produtos_mais_vendidos = ["Nenhum produto foi vendido"]
    return produtos_mais_vendidos
            
# Função para calcular a quantidade vendida de cada produto
def calcular_qtd_vendida_de_cada_produto(vendas):
    qtd_por_item = {}
    for venda in vendas:
        for produto in venda:
            if produto in qtd_por_item:
                qtd_por_item[produto] += 1
            else:
                qtd_por_item[produto] = 1
    return qtd_por_item

# Função para calcular o faturamento total das vendas
def calcular_faturamento(totais_venda):
    faturamento = 0
    for valor in totais_venda:
        faturamento += valor
    return faturamento

# Função que calcula o total de cada venda
def calcular_total_de_cada_venda(precos, vendas):
    totais_venda = []
    for venda in vendas:
        valor_desta_venda = 0
        for produto in venda:
            valor_desta_venda += precos.get(produto)
        totais_venda.append(round(valor_desta_venda, 1))
    return totais_venda

# Função principal
def main():
    precos = {
        "arroz": 22.5,
        "feijao": 9.8,
        "leite": 4.7,
        "pao": 1.5
    }
    
    vendas = [
        ["arroz", "feijao", "feijao", "leite"],
        ["pao", "pao", "pao", "leite"],
        ["arroz", "leite"],
        ["feijao", "feijao", "feijao"]
    ]
    
    totais_venda = calcular_total_de_cada_venda(precos, vendas)
    faturamento_total = calcular_faturamento(totais_venda)
    qtd_por_item = calcular_qtd_vendida_de_cada_produto(vendas)
    mais_vendido = encontrar_produto_mais_vendido(qtd_por_item)
    mais_faturado = produto_com_maior_faturamento(qtd_por_item, precos)
    ticket_medio = faturamento_total / len(vendas)
    print(gerar_relatorio(totais_venda, faturamento_total, qtd_por_item, mais_vendido, mais_faturado, ticket_medio))

# Programa principal
if __name__ == "__main__":
    main()