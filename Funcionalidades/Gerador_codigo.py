class Codigo: #Gera um codigo de produto/funcionario/conta autoincrementavel
    def __init__(self):
        self.codigo = 0
            
    def pro_num(self):
        self.codigo +=1
        return self.codigo