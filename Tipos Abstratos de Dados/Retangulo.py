from Ponto import Ponto
import math

class Retangulo:
    # Método construtor
    def __init__(self, largura: float, altura: float, canto_sup_esq: Ponto):
        self.largura = largura
        self.altura = altura
        self.canto_sup_esq = canto_sup_esq
        
    # Método para calcular e retornar a área
    def area(self) -> float:
        return round(self.largura * self.altura, 2) # Largura seria a nossa base
    
    # Método para calcular e retornar o perímetro
    def perimetro(self) -> float:
        return round(2 * (self.altura + self.largura), 2)
    
    # Método para aumentar o tamanho do retângulo
    def aumentar(self, altura: float, largura: float) -> float: # Essa altura e largura é como se fossem o p: Ponto
        self.largura += largura # Ao definir quanto você quer aumentar de largura ou altura
        self.altura += altura   # Atribuimos esse valor a variável original, aumentando o tamanho do retângulo
    
    # Método para retornar a coordenada do centro do retangulo
    def coord_centro(self) -> Ponto:
        xc = round(self.canto_sup_esq.x + self.largura / 2, 2) #xc = x do centro
        yc = round(self.canto_sup_esq.y - self.altura / 2, 2)
        return Ponto(xc, yc)
    
    # Se fosse para o canto superior esquerdo usariamos:
    # return Ponto(self.canto.x - self.l / 2, self.canto.y - self.h / 2)