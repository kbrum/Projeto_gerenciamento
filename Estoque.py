from Funções_basicas import Funções_basicas
class Estoque:
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

    def menu_estoque(): #pergunta ao usuario se quer voltar ao menu 
        while True:
            try:
                Funções_basicas.limpar_tela()
                Estoque.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    Funções_basicas.limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de estoque
                    Funções_basicas.limpar_tela()
                    Estoque.main_estoque()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Estoque.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def Produtos_em_falta():#mostra os produtos em falta
        if Estoque.em_falta:
            print('\nOs produtos em falta são:')
            for produtos_em_falta in Estoque.em_falta:
                print(f'.{produtos_em_falta}')
        else:
            Funções_basicas.limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
                
    def mostra_estoque(): #mostra todo o estoque
        if Estoque.produtos_em_estoque:
            print('\nProdutos em estoque:')
            for produtos in Estoque.produtos_em_estoque:
                print(f'.{produtos}')
        else:
            Funções_basicas.limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
            
    def mostrar_opcoes_estoque(): #mostra a opções q o usuario pode escolher
        print('\n1 - Ver todos')
        print('2 - Produtos em falta')
        print('3 - Voltar ao menu inicial')

    def checagem_estoque(): #faz a checagem doq foi escolhido entre os mostrados acima
        while True:
            try:
                print('\nEscolha uma opção')
                
                escolha = input('\n-------------> ').strip
                
                if not escolha:
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    Estoque.mostrar_opcoes_estoque()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)
                
                if escolha == 1:
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    Estoque.mostra_estoque()
                    Estoque.menu_estoque()
                    break
                
                elif escolha == 2:
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    Estoque.Produtos_em_falta()
                    Estoque.menu_estoque()
                    break
                
                elif escolha == 3:
                    Funções_basicas.limpar_tela()
                    Main.Main()
                    break
            
            except:
                Funções_basicas.limpar_tela()
                Estoque.name_app()
                Estoque.mostrar_opcoes_estoque()
                Funções_basicas.erro_de_valor()
        
    def main_estoque(): #executa todas as funções na ordem certa
        Funções_basicas.limpar_tela()
        Estoque.name_app()
        Estoque.mostrar_opcoes_estoque()
        Estoque.checagem_estoque()
        
    def executar_programa(): #mostra o programa na tela
        Estoque.main_estoque()
        
Estoque.executar_programa() #usado para testes unitarios (Por padrao desabilitado)
