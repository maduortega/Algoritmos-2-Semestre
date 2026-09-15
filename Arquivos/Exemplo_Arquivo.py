# Bloco de leitura de arquivo
with open('Alunos.txt', 'r') as Arquivo: # 'r' Aberto para leitura
    
    aprovados = 0
    reprovados = 0
    
    for linha in Arquivo:
        linha = linha.strip() # Strip tira os espaços sobrando
        nome, nota1, nota2 = linha.split(';') # Cria uma tupla com os dados (desacoplar) e o Split realiza um corte onde houver ;
        
        if (float(nota1) + float(nota2)) / 2 >= 7.0: # Nota está como str, temos que converter para int, nas demais linguagens usamos (float)nota1
            print(f'O Aluno: {nome} Está aprovado, com a média {(float(nota1) + float(nota2)) / 2}')
            aprovados += 1
            print()
        else:
            print(f'O Aluno: {nome} Está reprovado, com a média {(float(nota1) + float(nota2)) / 2}')
            reprovados += 1
            
    print()
    print(f'Total aprovados: {aprovados}')
    print(f'Total reprovados: {reprovados}')