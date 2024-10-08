import Funções_basicas

def name_app(): #titulo
    print('''
███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
█████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
    
saldo = 1000.00 #variavel que guarda o saldo
despesas = [] #lista das despesas

def menu_financeiro(): #pergunta ao usuario se quer voltar ao menu 
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
            
            elif menu == 1: # volta ao menu de financeiro
                Funções_basicas.limpar_tela()
                main_financeiro()
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            input('\n(Digite Enter para continuar)')

def cadastrar_outra_despesa():
    ...

def cadastrar_despesa():
    ...

def mostrar_saldo(): #mostra o saldo
    print(f'\nSeu saldo é de R${saldo}')

def mostrar_despesas(): # mostra as despesas
    print('\nSuas depesas:')
    for despesa in despesas:
        print(f'.{despesa}')


            
def mostrar_opcoes_financeiro(): #mostra as opções que o usuario pode escolher
    print('\n1 - Ver Saldo')
    print('2 - Ver despesas')
    print('3 - Cadastrar despesa')
    print('4 - Voltar ao menu inicial')

def checagem_financeiro(): #faz a checagem doq foi escolhido entre os mostrados acima
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
               name_app()
               cadastrar_despesa()
               cadastrar_outra_despesa() 
            
            elif escolha_financeiro == 4:
                Funções_basicas.limpar_tela()
                print('não implementado ainda')
                break

        except:
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_financeiro()
            Funções_basicas.erro_de_valor()
            checagem_financeiro()
            break
    
def main_financeiro(): #executa todas as funções na ordem certa
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opcoes_financeiro()
    checagem_financeiro()
    
def executar_programa(): #mostra o programa na tela
    main_financeiro()

#executar_programa() #usado para testes unitarios