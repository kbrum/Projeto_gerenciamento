from Funções_basicas import Funções_basicas

class codigo: #gera um codigo de pedido autoincrementavel
        def __init__(self):
            self.codigo = 0
            
        def pro_num(self):
            self.codigo +=1
            return self.codigo

class Pedidos:
    
    def name_app():
        print('''
    ██████╗░███████╗██████╗░██╗██████╗░░█████╗░░██████╗
    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████╗░░██║░░██║██║██║░░██║██║░░██║╚█████╗░
    ██╔═══╝░██╔══╝░░██║░░██║██║██║░░██║██║░░██║░╚═══██╗
    ██║░░░░░███████╗██████╔╝██║██████╔╝╚█████╔╝██████╔╝
    ╚═╝░░░░░╚══════╝╚═════╝░╚═╝╚═════╝░░╚════╝░╚═════╝░         
              ''')
        
    class pedido:
        def __init__(self):
            pass