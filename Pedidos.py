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
        def __init__(self,nome_cliente,tipo_produto,numero_contato,valor_pedido,forma_pagamento,):
            self.nome = nome_cliente
            self.tipo = tipo_produto
            self.contato = numero_contato
            self.valor = valor_pedido
            self.pagamento = forma_pagamento
      
    def menu_pedidos(): #pergunta ao usuario se quer voltar ao menu Pedidos
        while True:
            try:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    Funções_basicas.limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de Pedidos
                    Funções_basicas.limpar_tela()
                    Pedidos.main_Pedidos()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)') 
      
    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                print(f'\nO {tipo} do seu produto não pode ficar em branco.')  
            
    def solicitar_pagamento(): #Pergunta a forma de pagamento
        ...
    
    def solicitar_valor():  # Função para garantir que o preço seja numérico
        while True:
            try:
                print('\nQual o valor do seu? (Insira apenas números)')
                preço = float(input('\n------------->').strip())
                if preço > 0:
                    return preço
                else:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    print('O valor do produto deve ser positivo.')
            except ValueError:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                Funções_basicas.preço_erro()
    
    def mostrar_opcoes():
        print('\n1 - Ver pedidos')
        print('2 - Cadastrar pedido')
        print('3 - Finalizar pedido')
        print('4 - voltar ao menu principal')
    
    def checagem():
        while True:
            try:
                print('\nEscolha uma opção')
                escolha_Pedidos = int(input('\n-------------> '))
                
                if escolha_Pedidos == 1:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Pedidos.mostrar_pedidos()
                    print('\n')
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha_Pedidos == 2:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Pedidos.Produtos_em_falta()
                    print('\n')
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha_Pedidos == 3:
                    Funções_basicas.limpar_tela()
                    Main.Main()
                    break
            
            except:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                Pedidos.mostrar_opcoes()
                Funções_basicas.erro_de_valor()
                Pedidos.checagem()
                break
    
    def main_pedidos():
        Funções_basicas.limpar_tela()
        Pedidos.name_app()
    
    def executar_programa():
        Pedidos.main_pedidos()

Pedidos.executar_programa()