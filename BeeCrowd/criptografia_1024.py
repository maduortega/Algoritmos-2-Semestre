# Função criptografar 3 posições para frente
def criptografar(texto: str):
    aux = ''
    aux2 = ''
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra)
            aux += chr(codigo + 3)
        else: 
            aux += letra

# Função para inverter a criptografia            
    invertida = ''
    for i in range(len(aux) - 1, -1, -1):
        # [:: - 1] - Inverter qualquer coisa (lista, string, elementos)
        invertida += aux[i]

# Função para pegar as metades       
    texto_metade = ''
    texto_metade2 = ''
    
    for i in range(len(invertida) // 2):
        texto_metade2 += invertida[i]
        
    for i in range(len(invertida) // 2, len(invertida)):
        texto_metade += chr(ord(invertida[i]) - 1)
    
    texto_cripto = texto_metade2 + texto_metade

    return texto_cripto

# Função principal
def main():
    N = int(input('Informe a quantidade: '))
    for i in range(N):
        texto = input('Informe uma frase: ')
        print(criptografar(texto))

# Programa principal
if __name__ == '__main__':
    main()