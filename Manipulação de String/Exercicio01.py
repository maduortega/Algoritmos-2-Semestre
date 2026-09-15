# Função para criptografar um texto
def criptografar(texto: str, deslocamento: int) -> str:
    aux = '' # As aspas permitem guardar mais de um caractere dentro da aux
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra)
            aux += chr(((codigo - 97 + deslocamento) % 26) + 97) # ((('Z - A' + Qtd desloc) % N letras alfabeto) + 'A') 97 pois estamos trabalhamos com letras minúsculas
        else:
            aux += letra # Se não for letra, o caractere continua como ele estava
    return aux # Chr converte o cálculo feito em string

# Função descriptografar
def descripto(texto_cripto: str, deslocamento: int) -> str:
    return criptografar(texto_cripto, - deslocamento)

# Funçaõ principal
def main():
    texto = input('Informe uma frase: ').lower() 
    deslocamento = int(input('Deslocamento: '))
    
    texto_cripto = criptografar(texto, deslocamento)
    print(texto_cripto)
    
    texto_descripto = descripto(texto_cripto, deslocamento)
    print(texto_descripto)

# Programa principal    
if __name__ == '__main__':
    main()