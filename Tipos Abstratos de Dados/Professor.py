class Professor:
    # Método construtor
    def __init__(self, nome: str, n_aulas: int, hr_aula: float, titulo: str, hr_extra: str):
        self.nome = nome
        self.n_aulas = n_aulas
        self.hr_aula = hr_aula
        self.titulo = titulo
        self.hr_extra = hr_extra
        
    def calcular_sl_base(self):
        salario = self.n_aulas * 4.5 * self.hr_aula
        if self.titulo == 'mestre':
            salario = salario * 1.085 # Aumento de 8,5%
        elif self.titulo == 'doutor':
            salario = salario * 1.12
        else:
            salario = salario
        return salario
    
    def calcular_hora_atividade(self):
        salario_2 = self.calcular_sl_base() # Passando o método calc_sl_base para este
        if self.hr_extra == 'sim':
            salario_2 = salario_2 * 1.05
        else:
            salario_2 = salario_2
        return salario_2
            
    def salario_bruto(self):
        total = self.calcular_hora_atividade()
        dsr = total * (1/6)
        salario_bruto = round(total + dsr, 2)
        return salario_bruto