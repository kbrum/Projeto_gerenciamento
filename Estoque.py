import Funções_basicas

def name_app(): # titulo    
    print('''
███████╗░██████╗████████╗░█████╗░░██████╗░██╗░░░██╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██║░░░██║██╔════╝
█████╗░░╚█████╗░░░░██║░░░██║░░██║██║██╗██║██║░░░██║█████╗░░
██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║╚██████╔╝██║░░░██║██╔══╝░░
███████╗██████╔╝░░░██║░░░╚█████╔╝░╚═██╔═╝░╚██████╔╝███████╗
╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝''')

em_falta = ['Produto 1', 'Produto 2', 'Produto 3'] #lista de produtos em falta
produtos_em_estoque = ['Produto 1', 'Produto 2', 'Produto 3'] #todos os produtos

def menu_estoque(): #pergunta ao usuario se quer voltar ao menu 
    while True:
        try:
            print('Deseja voltar ao menu? ')
            print('1 - Sim')
            print('2 - Não')
            menu = int(input('\n-------------> '))
            
            if menu == 2:
                Funções_basicas.limpar_tela()
                print('Finalizado')
                break
            
            elif menu == 1:
                Funções_basicas.limpar_tela()
                main_estoque()
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                Funções_basicas.erro_de_valor()

        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()

def Produtos_em_falta(): #mostra os produtos em falta
    print('\nOs produtos em falta são:')
    for produtos_em_falta in em_falta:
        print(f'.{produtos_em_falta}')
        
def todos_em_estoque(): #mostra todo o estoque
    print('\nProdutos em estoque:')
    for produtos in produtos_em_estoque:
        print(f'.{produtos}')
        
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

#executar_programa() #usado para testes unitarios
