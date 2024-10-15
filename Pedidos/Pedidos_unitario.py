from Funcionalidades.Utils import *
from Funcionalidades.Geradorores import *
from .Controle import *
from .Doces import *
from .Salgados import *

class Pedidos: #Pedidos
    def name_app():
        print('''
    ██████╗░███████╗██████╗░██╗██████╗░░█████╗░░██████╗
    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████╗░░██║░░██║██║██║░░██║██║░░██║╚█████╗░
    ██╔═══╝░██╔══╝░░██║░░██║██║██║░░██║██║░░██║░╚═══██╗
    ██║░░░░░███████╗██████╔╝██║██████╔╝╚█████╔╝██████╔╝
    ╚═╝░░░░░╚══════╝╚═════╝░╚═╝╚═════╝░░╚════╝░╚═════╝░''')
    
    def mostrar_opcoes(): # mostra as oções que podem ser escolhidas
        print('\n1 - Seção de doces')
        print('2 - Seção de salgados')
        print('3 - Fazer pedido')
        print('4 - Voltar ao menu principal')

    def checagem(): # checa a opção q o usuario escolheu
        while True:
            try:
                print('\nEscolha uma opção')
                escolha = int(input('\n-------------> '))
                
                if escolha == 1:
                    limpar_tela()
                    Doces.executar_programa()
                    Pedidos.executar_programa()                  
                    break
                
                elif escolha == 2:
                    limpar_tela()
                    Salgados.executar_programa()
                    Pedidos.executar_programa() 
                    break
                
                elif escolha== 3:
                    Controle_pedido.fazer_pedido(Pedidos, 'Pedidos')
                    Pedidos.executar_programa()
                    break                
                
                elif escolha == 4:
                    limpar_tela()
                    break
            
            except ValueError:
                limpar_tela()
                Pedidos.name_app()
                Pedidos.mostrar_opcoes()
                erro_de_valor()
                Pedidos.checagem()
            
    def executar_programa(): # mostra na tela
        limpar_tela()
        Pedidos.name_app()
        Pedidos.mostrar_opcoes()
        Pedidos.checagem()

#Pedidos.executar_programa() # usado para testes unitarios