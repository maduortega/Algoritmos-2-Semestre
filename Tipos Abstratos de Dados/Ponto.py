import math

class Ponto:
    # Método construtor
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
        
    # Método para calcular e retornar a distância entre dois pontos
    def calcular_dist(self, p: 'Ponto') -> float: # O self está puxando o x e y da classe, mas o x2 e y2 não vem da classe e sim do outro arquivo
        return round(math.hypot(self.x - p.x, self.y - p.y), 2)
    
    # Método para calcular e retornar a distância de um ponto até a origem
    def dist_origem(self) -> float:
        return round(math.hypot(self.x, self.y), 2) # self.x - 0, self.y - 0
    
    # O str retorna o endereço de memória (não em hexadecimal)
    # Sobreposição de método ou override
    def __str__(self):
        return f'({self.x}, {self.y})' # Agora ao printar o 'pontos' no for, temos seus valores e não um hexadecimal