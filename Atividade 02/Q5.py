            
# Função que gera o relatório final
def gerar_relatorio(por_aluno, aula_com_mais_faltas, aluno_com_maior_preseca, aluno_com_mais_falta, media_de_presenca):
    relatorio = {
        "por_aluno": por_aluno,
        "aula_mais_faltas": aula_com_mais_faltas,
        "melhor_presenca": aluno_com_maior_preseca,
        "mais_faltas": aluno_com_mais_falta,
        "presenca_media_turma": media_de_presenca
    }
    print(relatorio)
            
            
# Função que calcula a média de presença da turma
def calcular_media_de_presenca(presencas, qtd_aulas):
    lista_aulas = [0] * qtd_aulas # Isso vai criar uma lista na qual o tamanho é o len das aulas
    cont = 0                      # e todos esses seus indices serão iguais a 0
    media = 0
    
    for aluno in presencas.values():
        for i in range(len(aluno)):
            if aluno[i] == "P":
                lista_aulas[i] += 1
        cont += 1
    
    for i in range(len(lista_aulas)):
        media += ((lista_aulas[i] / cont) / qtd_aulas) * 100
    return media
            
# Função que calcula o aluno com mais faltas
def calcular_aluno_com_mais_falta(por_aluno):
    aluno = []
    maior = 0
    
    for nome, info in por_aluno.items():
        if info.get("F") != None:
            if info.get("F") == maior:
                aluno.append(nome)
            if info.get("F") > maior:
                aluno = [nome]
                maior = info.get("F")
    if len(aluno) == 0 or maior == 0:
        aluno = ["Nenhum aluno possui falta"]
    return aluno         
            
# Função que calcula o aluno com mais presencas
def calcular_aluno_com_maior_presenca(por_aluno):
    aluno = []
    maior = 0
    
    for nome, info in por_aluno.items():
        if info.get("P") != None:
            if info.get("P") == maior:
                aluno.append(nome)
            if info.get("P") > maior:
                aluno = [nome]
                maior = info.get("P")
    if len(aluno) == 0 or maior == 0:
        aluno = ["Nenhum aluno possui presença"]
    return aluno
           
# Função que calcula a aula com mais faltas
def calcular_aula_com_mais_faltas(aulas, presencas):
    faltas = [0] * len(aulas)
    maior = 0
    aula_com_mais_falta = []
    
    for aluno in presencas.values():
        for i in range(len(aluno)):
            if aluno[i] == "F":
                faltas[i] += 1
                if faltas[i] == maior and aulas[i] not in aula_com_mais_falta:
                    aula_com_mais_falta.append(aulas[i])
                if faltas[i] > maior:
                    maior = faltas[i]
                    aula_com_mais_falta = [aulas[i]]
    if len(aula_com_mais_falta) == 0:
        aula_com_mais_falta = ["Nenhuma falta registrada"]
    return aula_com_mais_falta
    
# Função que calcula o total de presenças de cada aluno
def gerar_dicionario_por_aluno(presencas):
    aux = {"P": 0, "F": 0, "perc": 0, "situacao": " "}
    por_aluno = {}
    
    for nome, aula in presencas.items():
        for status in aula:
            if status == "P":
                aux["P"] += 1
                aux["perc"] += (1 / len(aula) * 100)
            else:
                aux["F"] += 1
        if aux["perc"] >= 75:
            aux["situacao"] = "APROVADO"
        else:
            aux["situacao"] = "REPROVADO"
        por_aluno[nome] = aux
        aux = {"P": 0, "F": 0, "perc": 0, "situacao": " "}
    return por_aluno
                
# Função principal
def main():
    aulas = ["A1", "A2", "A3", "A4", "A5"]
    
    presencas = {
        "Ana": ["P", "P", "F", "P", "P"],
        "Bruno": ["P", "F", "F", "P", "F"],
        "Carla": ["P", "P", "P", "P", "P"],
        "Diego": ["F", "F", "P", "F", "P"]
    }
    
    por_aluno = gerar_dicionario_por_aluno(presencas)
    aula_com_mais_faltas = calcular_aula_com_mais_faltas(aulas, presencas)
    aluno_com_maior_preseca = calcular_aluno_com_maior_presenca(por_aluno)
    aluno_com_mais_falta = calcular_aluno_com_mais_falta(por_aluno)
    media_de_presenca = calcular_media_de_presenca(presencas, len(aulas))
    
    relatorio = gerar_relatorio(por_aluno, aula_com_mais_faltas, aluno_com_maior_preseca, aluno_com_mais_falta, media_de_presenca)
# Programa principal
if __name__ == "__main__":
    main()
