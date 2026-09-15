from random import randint

def gerar_lista1():
    lista_p1 = []
    
    for _ in range(3):
        nome, nota = input('Informe o nome do aluno: '), ((randint(0,10)))
        t = (nome, nota) 
        lista_p1.append(t)
    return lista_p1

def gerar_lista2(p1):
    lista_p2 = []
    
    for i in range(len(p1)):
        aluno, nota = p1[i] # Desempacota os valores, coloca o 1° valor na 1° variável e o 2° na 2°
        nome, nota = (aluno), ((randint(0,10)))
        t = (nome, nota)
        lista_p2.append(t)
    return lista_p2

def melhoraram(p1, p2):
    melhor = []
    
    for i in range(len(p1)): # Não precisamos das duas listas, pois o tamanho da p1 e da p2 são iguais
        aluno, nota1 = p1[i] # Desempacotando os valores das duas listas de tuplas
        aluno, nota2 = p2[i] # O aluno é o mesmo, por isso a mesma variável
        if nota2 > nota1:
            melhor.append(aluno)
    return melhor

def pioraram(p1, p2):
    pior = []
    
    for i in range(len(p1)):
        aluno, nota1 = p1[i] # Desempacotando os valores das duas listas de tuplas
        aluno, nota2 = p2[i] # O aluno é o mesmo, por isso a mesma variável
        if nota2 < nota1:
            pior.append(aluno)
    return pior

def manteve(p1, p2):
    igual = []
    
    for i in range(len(p1)):
        aluno, nota1 = p1[i] # Desempacotando os valores das duas listas de tuplas
        aluno, nota2 = p2[i] # O aluno é o mesmo, por isso a mesma variável
        if nota2 == nota1:
            igual.append(aluno)
    return igual

# Função Main
def main():
    
    p1 = gerar_lista1()
    p2 = gerar_lista2(p1)

    print()
    print(f'Aluno(s) e suas notas na 1° prova: {p1}')
    print(f'Aluno(s) e suas notas na 2° prova: {p2}\n')
    
    melhor = melhoraram(p1, p2)    
    pior = pioraram(p1, p2)
    igual = manteve(p1, p2)
    
    print(f'Aluno(s) que melhoraram sua nota: {melhor}')
    print(f'Aluno(s) que pioraram sua nota: {pior}')
    print(f'Aluno(s) que mantiveram sua nota: {igual}')
    
# Programação principal
if __name__ == '__main__':
    main()