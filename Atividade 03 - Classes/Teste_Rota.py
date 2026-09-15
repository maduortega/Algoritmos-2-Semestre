from Rota import Rota

lista = []
qtd = int(input('Informe a quantidade de rotas: '))

for _ in range(qtd):
    nome = input('Informe o nome da rota: ')
    dist_km = float(input('Informe a distância do trecho em km: '))
    vel_kmh = float(input('Informe a velocidade média do trecho em km/h: '))
    semaforo = int(input('Informe a quantidade de semáforos do trecho: '))
    delay_s = float(input('Informe o delay médio do sinal: '))
    
    trecho = []
    
    trecho.append({ # Adiciona um dicionário para a lista
        'dist_km': dist_km,
        'vel_kmh': vel_kmh,
        'semaforo': semaforo
    })
    
    rota = Rota(nome, trecho, delay_s) # Variável de referência recebe a rota para poder por na lista
    lista.append(rota)
    
# Ordenar da mais rápida para a mais lenta e mostrar um ranking 
lista_ordenada = []

for ordenar in lista:
    valores = [ordenar.nm_rota, ordenar.tempo_total_min(), ordenar.velocidade_media_kmh()] # Cria uma lista com os valores precisos para o método
    lista_ordenada.append(valores) # Append nesses valores, lista só aceita 1 valor
    
ordenado = rota.bolha(lista_ordenada) # Depois que ordenar, guarda aqui

rank = 1    
for rota in lista_ordenada: # Faz outro for para percorrer agora a lista ordenada
    print(f'Rank: {rank} | Rota: {rota[0]} | Tempo total: {rota[1]} | Velocidade média: {rota[2]}kmh') # FINALMENTE PRINTA A LISTA ORDENADA
    rank += 1