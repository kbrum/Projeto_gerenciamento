
class Nova_conta: #contrutor de uma nova conta
        def __init__(self,nome,tipo,dado,valor,data,codigo,status):
            self.nome = nome
            self.tipo = tipo
            self.dado = dado
            self.valor = valor
            self.codigo = codigo
            self.status = status
            self.data = data
        
        def finalizar_conta(self): # finalizador de pedidos (altera o self.status de true para false ('conta paga/recebida ou pedente'))
            if self.status:  # Verifica se o pedido está ativo
                
                self.status = False
                
            else:
                
                print(f"a conta {self.nome} de codigo {self.codigo} ja foi fechada.")