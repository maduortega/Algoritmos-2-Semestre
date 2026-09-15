class Aluno: # Classes costumam ter a primeira letra em maiúsculo
    # Atributos (variável de instância) do objeto
    nome: str # Usamos esse atributo só para entender oq a função faz, não é necessário tê-los
    ra: int
    nota1: float
    nota2: float
    
    # Construtor (Gera o objeto e coloca dentro desse objeto uma cópia dos seus atributos)
    def __init__(self, nome: str = '', ra: int = 0, nota1: float = 0, nota2: float = 0):
        self.nome = nome # O self pega o atributo e atribui para ele o parâmetro dentro da função
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        
    # Método para calcular e retornar a média
    def calcular_media(self) -> float: # Sempre que houver manipulação do objeto (acessar algo que faz parte do objeto) devemos ter o self
        return (self.nota1 + self.nota2) / 2
        
    # Método para retornar a situação do aluno (aprovado ou reprovado)
    def situacao(self) -> str:
        if self.calcular_media() >= 6.75:
            return 'Aprovado'
        return 'Reprovado'