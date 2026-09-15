from Emprestimo import Emprestimo

lista = []
qtd = int(input('Informe a quantidade de clientes: '))

for _ in range(qtd):
    nm_cli = input('Informe o nome do(a) cliente: ')
    vl_finan = float(input('Informe o valor total financiado: '))
    tx_juros_mensal = float(input('Informe a taxa de juros mensal (em %): ')) # Exemplo: 2, 1.5
    n_parcelas = int(input('Informe o número total de parcelas: '))
    id_emprestimo = input('Informe o identificador do empréstimo: ')
    
    lista.append(Emprestimo(nm_cli, vl_finan, tx_juros_mensal, n_parcelas, id_emprestimo))
    emprestimo = (Emprestimo(nm_cli, vl_finan, tx_juros_mensal, n_parcelas, id_emprestimo)) # Para usar o bolha
    
print('-' * 90)

plano = 1
print(f'Painel Financeiro - Parcelas e Juros por Empréstimo (Ranking)')
print()
lista_ordenada = []

for ordenar in lista:
    valores = [ordenar.id_emprestimo, ordenar.valor_parcela(), ordenar.total_juros_pago(), ordenar.custo_total()]
    lista_ordenada.append(valores)
    
ordenado = emprestimo.bolha(lista_ordenada)

for cliente in lista_ordenada:
    print(f'Cliente: {plano} - Id: {cliente[0]} | Parcela: R${cliente[1]} | Juros Totais: R${cliente[2]} | Custo Total: R${cliente[3]}')     
    plano += 1

# print(f'Cliente: {plano} - Id: {cliente.id_emprestimo} | Parcela: R${cliente.valor_parcela()} | Juros Totais: R${cliente.total_juros_pago()} | Custo Total: R${cliente.custo_total()}') print sem o rank
    
print('-' * 90)

plano = 1
print(f'Painel Financeiro - Saldo Devedor (12ª Parcela)')
print()

for devedor in lista:
    print(f'Cliente: {plano} - Id {devedor.id_emprestimo} | Saldo devedor após a 12° parcela: R${devedor.saldo_dev()}')
    plano += 1