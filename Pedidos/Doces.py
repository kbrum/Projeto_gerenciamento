from .Controle import *
from Funcionalidades.Utils import *

class Doces:
    def name_app():
        print('''
    ██████╗░░█████╗░░█████╗░███████╗░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║░░██║██║░░██║██║░░╚═╝█████╗░░╚█████╗░
    ██║░░██║██║░░██║██║░░██╗██╔══╝░░░╚═══██╗
    ██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝
    ╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░''')
    
    def todos_doces(): #mostra todos os pedidos ja feitos na seção doces
        if len(Controle_pedido.pedidos_doces) == 0: # checa se a lista esta vazia
            print('\nNenhum pedido cadastrado.')
        else:
            print('\nLista de pedidos feitos:')
            for i, pedido in enumerate(Controle_pedido.pedidos_doces, start=1):
                status_pedido = 'Pedido ativo' if pedido.status else 'Pedido finalizado' # Fatora a string para exibir pedido ativo ou finalizado em vez de true ou false
                print(f'\n{i}. Nome: {pedido.nome} | Tipo: {pedido.tipo} | Quantidade: {pedido.quantidade} | Numero para contato: {pedido.contato} | Valor do pedido: R${pedido.valor} | Forma de pagamento: {pedido.pagamento} | Código: {pedido.codigo} | Status do pedido: {status_pedido}')
                #exibe na tela os pedidos
                
        input('\n(Digite Enter para continuar)')
        
    def doces_ativos(): #mostra apenas os pedidos da seção doce que estão ativos
        if len(Controle_pedido.pedidos_doces) == 0:
            print('\nNenhum pedido ativo ou cadastrado')
        else:
            print('\nLista de pedidos feitos:')
            for i, pedido in enumerate(Controle_pedido.pedidos_doces, start=1):
                status_pedido = 'Pedido ativo' if pedido.status else 'Pedido finalizado' # Fatora a string para exibir pedido ativo ou finalizado em vez de true ou false
                if status_pedido == 'Pedido ativo': # verifica se o pedido esta ativo ou finalizado
                    print(f'\n{i}. Nome: {pedido.nome} | Tipo: {pedido.tipo} | Quantidade: {pedido.quantidade} | Numero para contato: {pedido.contato} | Valor do pedido: R${pedido.valor} | Forma de pagamento: {pedido.pagamento} | Código: {pedido.codigo} | Status do pedido: {status_pedido}')
                else:
                    print('\nNenhum pedido ativo ou cadastrado')
        input('\n(Digite Enter para continuar)')
        
    def mostrar_opcoes():
        print('\n1 - Ver todos os pedidos')
        print('2 - Ver pedidos ativos')
        print('3 - Finalizar pedido')
        print('4 - Voltar ao menu pedidos')
    
    def checagem():
        while True:
            try:
                print('\nEscolha uma opção')
                escolha = int(input('\n-------------> '))
                
                if escolha == 1:
                    limpar_tela()
                    Doces.name_app()
                    Doces.todos_doces()
                    Doces.executar_programa()                  
                    break
                
                elif escolha == 2:
                    limpar_tela()
                    Doces.name_app()
                    Doces.doces_ativos()
                    Doces.executar_programa()
                    break
                
                elif escolha== 3:
                    limpar_tela()
                    Doces.name_app()
                    Controle_pedido.finalizar_pedido_doce(Doces) # finalizar pedidos da seção doces
                    Doces.executar_programa()
                    break                
                
                elif escolha == 4:
                    limpar_tela()
                    break
            
            except ValueError:
                limpar_tela()
                Doces.name_app()
                Doces.mostrar_opcoes()
                erro_de_valor()
                   
    def executar_programa():
        limpar_tela()
        Doces.name_app()
        Doces.mostrar_opcoes()
        Doces.checagem()
        