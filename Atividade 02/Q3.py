
# Função que calcula o faturamento total da loja
def calcular_faturamento(total_gasto_por_cliente):
    faturamento = 0
    for valor in total_gasto_por_cliente.values():
        faturamento += valor
    return faturamento

# Função para descobrir qual cliente mais gastou
def descobrir_cliente_que_mais_gastou(total_gasto_por_cliente):
    cliente_que_mais_gastou = []
    maior = 0
    for nome, valor_gasto in total_gasto_por_cliente.items():
        if valor_gasto == maior:
            cliente_que_mais_gastou.append(nome)
        if valor_gasto > maior:
            cliente_que_mais_gastou = [nome]
            maior = valor_gasto
    if maior == 0:
        cliente_que_mais_gastou = ["Nenhum cliente comprou nada"]
    return cliente_que_mais_gastou

# Função que calcula o total gasto por clientes
def calcular_total_gasto_por_cliente(pedidos):
    total_gasto_por_cliente = {}
    for pedido in pedidos.values():
        nome = pedido.get("cliente")
        produto = pedido.get("produtos")
        for valor in produto.values():
            if nome in total_gasto_por_cliente:
                total_gasto_por_cliente[nome] += valor
            else:
                total_gasto_por_cliente[nome] = valor            
    return total_gasto_por_cliente

# Função que calcula o total gasto por pedidos
def calcular_total_por_pedido(pedidos):
    valor_de_cada_pedido = {}
    for numero, pedido in pedidos.items():
        produto = pedido.get("produtos") # O get vai no dict e verifica se existe uma chave com esse nome, caso
        for valor in produto.values():   # tenha, retorna um valor, se tivesse entre aspas, ele entenderia que o
            if numero in valor_de_cada_pedido: # produto é a própria chave que ele vai buscar
                valor_de_cada_pedido[numero] += valor
            else:
                valor_de_cada_pedido[numero] = valor
    return valor_de_cada_pedido
            
# Função principal
def main():
    pedidos = {
        "P001": {"cliente": "Ana", "produtos": {"Mouse": 80, "Teclado": 120}},
        "P002": {"cliente": "Bruno", "produtos": {"Monitor": 700}},
        "P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40, "Mouse": 80}},
        "P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950}}   
    }

    print(f" Total gasto por pedido --> {calcular_total_por_pedido(pedidos)}")
    total_gasto_por_cliente = calcular_total_gasto_por_cliente(pedidos)
    print(f"Total gasto por cliente --> {total_gasto_por_cliente}")
    print(f"Cliente que mais gastou --> {descobrir_cliente_que_mais_gastou(total_gasto_por_cliente)}")
    print(f"Faturamento total da loja --> R${calcular_faturamento(total_gasto_por_cliente)}")

# Programa principal
if __name__ == "__main__":
    main()