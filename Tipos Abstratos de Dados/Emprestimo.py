class Emprestimo:
    # Método construtor
    def __init__(self, nome: str, valor_financiado: float, taxa_juros_mensal: float, n_parcelas: int, id_emprestimo: str):
        self.nome = nome
        self.valor_financiado = valor_financiado
        self.taxa_juros_mensal = taxa_juros_mensal
        self.n_parcelas = n_parcelas
        self.id_emprestimo = id_emprestimo
        
    # Método para calcular e retornar o valor da parcela (fixa) pelo método PRICE
    def valor_parcela(self):
        juros = self.taxa_juros_mensal / 100 # Transformando a % em decimal para calcular corretamente
        v_parcela = 0
        if self.taxa_juros_mensal == 0:
           v_parcela = round(juros / self.n_parcelas, 2)
        elif self.taxa_juros_mensal > 0:
            v_parcela = round(self.valor_financiado * (juros / (1 - (1 + juros) ** -self.n_parcelas)), 2)
        return v_parcela
    
    # Método para retornar o saldo devedor após o pagamento da k-ésima parcela (neste caso 12)
    def saldo_dev(self):
        juros = self.taxa_juros_mensal / 100
        parcela = self.valor_parcela()
        saldo = 0
        if self.taxa_juros_mensal > 0:
                devendo = round(self.valor_financiado * (1 + juros) ** 12 - parcela * ((1 + juros) ** 12 - 1) / juros, 2)
                saldo = devendo # Para quebrar uma linha no append, basta por \n ao final
        return saldo
                
    # Método para calcular e retornar o valor total de juros pagos ao final do financiamento
    def total_juros_pago(self):
        total_juros_pagos = 0
        parcela = self.valor_parcela()
        total_juros_pagos = round(self.n_parcelas * parcela - self.valor_financiado, 2)
        return total_juros_pagos
    
    # Método para calcular o custo total gasto pelo cliente
    def custo_total(self):
        custo = 0
        parcela = self.valor_parcela()
        custo = round(self.n_parcelas * parcela, 2)
        return custo
    
    # Método para ordenar os juros em ordem crescente (usando o método bolha)
    def bolha(self, lista_ordenada: float) -> list[int]:
        for _ in range(len(lista_ordenada)):
            for i in range(len(lista_ordenada) - 1):
                # Comparando pelo juros, que está no índice 2, assim não vamos ter confusões
                if lista_ordenada[i][2] > lista_ordenada[i + 1][2]: # < se quisermos decrescente
                    lista_ordenada[i], lista_ordenada[i + 1] = lista_ordenada[i + 1], lista_ordenada[i]
        return lista_ordenada