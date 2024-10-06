import Funções_basicas

def name_app():    
    print('''
███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
█████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
    
saldo = 1000.00
despesas = ['despesa 1', 'despesa 2', 'despesa 3']

def mostrar_saldo(): #mostra o saldo
    print(f'\nSeu saldo é de R${saldo}')

def mostrar_despesas(): # mostra as despesas
    print('\nSuas depesas:')
    for despesa in despesas:
        print(f'.{despesa}')

def menu_financeiro(): #pergunta ao usuario se quer voltar ao menu 
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
                main_financeiro()
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                Funções_basicas.erro_de_valor()

        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            
def mostrar_opcoes_financeiro(): #mostra as opções que o usuario pode escolher
    print('\n1 - Ver Saldo')
    print('2 - Ver despesas')
    print('3 - Voltar ao menu inicial')

def checagem_financeiro(): #faz a checagem doq foi escolido entre os mostrados acima
    while True:
        try:
            print('\nEscolha uma opção')
            escolha_financeiro = int(input('\n-------------> '))
            
            if escolha_financeiro == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_saldo()
                print('\n')
                menu_financeiro()
                break
            elif escolha_financeiro == 2:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_despesas()
                print('\n')
                menu_financeiro()
                break
            elif escolha_financeiro == 3:
                Funções_basicas.limpar_tela()
                print('não implementado ainda')
                break
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_financeiro()
                Funções_basicas.erro_de_valor()
                checagem_financeiro()
                break
        except:
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_financeiro()
            Funções_basicas.erro_de_valor()
            checagem_financeiro()
            break
    
def main_financeiro(): # executa todas as funções na ordem certa
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opcoes_financeiro()
    checagem_financeiro()
    
def executar_programa(): #mostra o programa na tela
    main_financeiro()

executar_programa() #usado para testes unitarios