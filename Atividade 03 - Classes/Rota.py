class Rota:
    
    # Método construtor
    def __init__(self, nm_rota: str, trecho: list[dict], delay_s: float): # Delay padrão: 45s
        self.nm_rota = nm_rota
        self.trecho = trecho
        self.delay_s = delay_s
        
    # Função para converter segundos em minutos  
    def converter_atraso(self):
        delay_min = 0
        delay_min = round(self.delay_s / 60, 2)
        return delay_min
    
    # Método para calcular o tempo total da rota em minutos:
    def tempo_total_min(self) -> float:
        tempo_h = 0
        paradas_min = 0
        tempo_total = 0
        total_semaforo = 0
        delay_min = self.converter_atraso()
        
        for dado in self.trecho:
            d_km = dado.get('dist_km')
            v_kmh = dado.get('vel_kmh')
            semaforo = dado.get('semaforo')
            
            tempo_h += d_km/v_kmh # Faz a soma de todo o cálculo (sinal de sumarizar)
            total_semaforo += semaforo
            
        paradas_min = semaforo * delay_min
        tempo_total = round(60 * tempo_h + paradas_min, 2)
        return tempo_total
    
    # Método para ordenar rotas pelo tempo em ordem crescente (usando o método bolha)
    def bolha(self, lista_ordenada: float) -> list[int]:
        for _ in range(len(lista_ordenada)):
            for i in range(len(lista_ordenada) - 1): # Se for de 0 a 9, vai até o 8 e não estoura pois chega até o limite da lista (9)
                # Comparando pelo tempo, que está no índice 1, assim não vamos ter confusões
                if lista_ordenada[i][1] > lista_ordenada[i + 1][1]: # < se quisermos decrescente
                    lista_ordenada[i], lista_ordenada[i + 1] = lista_ordenada[i + 1], lista_ordenada[i]
        return lista_ordenada
            
    # Método para calcular a velocidade média global da rota
    def velocidade_media_kmh(self) -> float:
        d_km = 0
        d_total = 0
        tempo_total = self.tempo_total_min()
        horas = 0
        v_media = 0
        
        for dado in self.trecho: # ou repete isso nos demais métodos ou cria um método só pra calcular isso
            d_km = dado.get('dist_km')
            d_total += d_km
            
        horas = tempo_total / 60
        v_media = round(d_total / horas, 2)
        return v_media
    
    # Função que verifica se atende uma janela (passar o parâmetro)
    def atende_janela(self, inicio_min: float, fim_min: float) -> bool:
        tempo_total = self.tempo_total_min()
        
        if tempo_total >= inicio_min and tempo_total <= fim_min:
            return True
    
    # Função que estima emissões (devemos passar o parâmetro no terminal, não puxamos da classe)
    def custo_emissao(self, kg_co2_km: float) -> float:
        d_km = 0
        d_total = 0
        emissao = 0
        
        for dado in self.trecho:
            d_km = dado.get('dist_km')
            d_total += d_km
            
        emissao = round(d_total * kg_co2_km, 2)
        return emissao