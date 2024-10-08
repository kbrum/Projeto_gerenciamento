import Funções_basicas

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
            name_app()
            print('\nDeseja voltar ao menu? ')
            print('1 - Sim')
            print('2 - Não')
            
            menu = input('\n-------------> ').strip()
            
            if not menu: # verifica se a entrada do menu não é vazia
                Funções_basicas.limpar_tela()
                name_app()
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
                main_estoque()
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            input('\n(Digite Enter para continuar)')

def Produtos_em_falta():#mostra os produtos em falta
    if em_falta:
        print('\nOs produtos em falta são:')
        for produtos_em_falta in em_falta:
            print(f'.{produtos_em_falta}')
    else:
        Funções_basicas.limpar_tela()
        name_app()
        print('\nNenhum produto cadastrado.')
        input('\nPressione Enter para continuar.')
            
def todos_em_estoque(): #mostra todo o estoque
    if produtos_em_estoque:
        print('\nProdutos em estoque:')
        for produtos in produtos_em_estoque:
            print(f'.{produtos}')
    else:
        Funções_basicas.limpar_tela()
        name_app()
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
            escolha_financeiro = int(input('\n-------------> '))
            
            if escolha_financeiro == 1:
                Funções_basicas.limpar_tela()
                name_app()
                todos_em_estoque()
                print('\n')
                menu_estoque()
                break
            
            elif escolha_financeiro == 2:
                Funções_basicas.limpar_tela()
                name_app()
                Produtos_em_falta()
                print('\n')
                menu_estoque()
                break
            
            elif escolha_financeiro == 3:
                Funções_basicas.limpar_tela()
                print('não implementado ainda')
                break
        
        except:
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_estoque()
            Funções_basicas.erro_de_valor()
            checagem_estoque()
            break
    
def main_estoque(): #executa todas as funções na ordem certa
    name_app()
    mostrar_opcoes_estoque()
    checagem_estoque()

def executar_programa(): #mostra o programa na tela
    main_estoque()

#executar_programa() #usado para testes unitarios (Por padrao desabilitado)
