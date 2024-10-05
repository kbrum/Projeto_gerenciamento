import Funções_basicas

def name_app():    
    print('''
███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
█████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
    
saldo = 1000
despesas = ['despesa 1', 'despesa 2', 'despesa 3']

def mostrar_despesas():
    for despesa in despesas:
        print(f'.{despesa}')

def mostrar_opces_financeiro(): #mostra as opções
    print('\n1 - Ver Saldo')
    print('2 - Ver despesas')
    print('3 - Voltar ao menu inicial')


def checagem_financeiro(): #faz a checagem doq foi escolido entre os mostrados acima
    while True:
        try:
            escolha_financeiro = int(input('\nEscolha uma opção: '))
            
            if escolha_financeiro == 1:
                print(saldo)
                break
            elif escolha_financeiro == 2:
                Funções_basicas.limpar_tela()
                mostrar_despesas()
                break
            elif escolha_financeiro == 3:
                Funções_basicas.limpar_tela()
                break
            else:
                Funções_basicas.erro_de_valor()
        except:
           Funções_basicas.erro_de_valor()
    
    
def main_financeiro():
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opces_financeiro()
    checagem_financeiro()