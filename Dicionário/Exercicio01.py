def filtrar(leads: list[dict]):
    for score in leads:
        if score.get('Score') >= 70: # Ou score['score'] (menos utilizado)
            print(score.get('Nome')) # Printo só o nome das pessoas com score >= 70

def taxa(leads: list[dict]):
    totais = {}
    ganho = {}
    
    for lead in leads:
        origem = lead.get('Origem')
        status = lead.get('Status')
        
        if origem not in totais:
            totais[origem] = 0
            ganho[origem] = 0
        
        totais[origem] += 1
        if status == 'Ganho':
            ganho[origem] += 1
            
    # Cálculo da taxa de conversão
    for origem in totais:
        t = totais.get(origem)
        g = ganho.get(origem)
        taxa = g / t if t > 0 else 0 # Executa se t for > 0 se não t é = 0 (taxa = 0)
        print(f'{origem} --> {(taxa * 100): .2f}%')

def main():
    leads = [
        {'Nome': 'Ana', 'Origem': 'Instagram', 'Score': 82, 'Status': 'Ganho'},
        {'Nome': 'Beto', 'Origem': 'Google', 'Score': 65, 'Status': 'Perdido'},
        {'Nome': 'Cris', 'Origem': 'Indicação', 'Score': 90, 'Status': 'Ganho'},
        {'Nome': 'Duda', 'Origem': 'Instagram', 'Score': 74, 'Status': 'Perdido'},
        {'Nome': 'Enzo', 'Origem': 'Google', 'Score': 71, 'Status': 'Ganho'}
    ]

    # Filtrando os leads com score >= 70
    filtrar(leads)
    print()
    
    # Taxa de conversão por origem
    taxa(leads)

# Programa principal
if __name__ == '__main__':
    main()
