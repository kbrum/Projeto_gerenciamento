from Funcionalidades.Utils import *

class Estoque: #menu de estoque
    def name_app(): # titulo    
        print('''
    ███████╗░██████╗████████╗░█████╗░░██████╗░██╗░░░██╗███████╗
    ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██║░░░██║██╔════╝
    █████╗░░╚█████╗░░░░██║░░░██║░░██║██║██╗██║██║░░░██║█████╗░░
    ██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║╚██████╔╝██║░░░██║██╔══╝░░
    ███████╗██████╔╝░░░██║░░░╚█████╔╝░╚═██╔═╝░╚██████╔╝███████╗
    ╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝''')

    em_falta = [] #lista de produtos em falta
    produtos_em_estoque = [] #todos os produtos

    def Em_falta():#mostra os produtos em falta
        if Estoque.em_falta:
            print('\nOs produtos em falta são:')
            for produtos_em_falta in Estoque.em_falta:
                print(f'.{produtos_em_falta}')
        else:
            limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
                
    def mostra_estoque(): #mostra todo o estoque
        if Estoque.produtos_em_estoque:
            print('\nProdutos em estoque:')
            for produtos in Estoque.produtos_em_estoque:
                print(f'.{produtos}')
        else:
            limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
            
    def mostrar_opcoes(): #mostra a opções q o usuario pode escolher
        print('\n1 - Ver todos')
        print('2 - Em falta')
        print('3 - Voltar ao menu inicial')

    def checagem(): #faz a checagem doq foi escolhido entre os mostrados acima
        while True:
            try:
                print('\nEscolha uma opção')
                
                escolha = input('\n-------------> ').strip()
                
                if not escolha:
                    limpar_tela()
                    Estoque.name_app()
                    Estoque.mostrar_opcoes_estoque()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)
                
                if escolha == 1:
                    limpar_tela()
                    Estoque.name_app()
                    Estoque.mostra_estoque()
                    Estoque.executar_programa()    
                    break
                
                elif escolha == 2:
                    limpar_tela()
                    Estoque.name_app()
                    Estoque.Em_falta()
                    Estoque.executar_programa()
                    break
                
                elif escolha == 3:
                    limpar_tela()
                    break
            
            except:
                limpar_tela()
                Estoque.name_app()
                Estoque.mostrar_opcoes()
                erro_de_valor()
        
    def executar_programa(): #mostra o programa na tela
        limpar_tela()
        Estoque.name_app()
        Estoque.mostrar_opcoes()
        Estoque.checagem()
        
#Estoque.executar_programa() #usado para testes unitarios (Por padrao desabilitado)
