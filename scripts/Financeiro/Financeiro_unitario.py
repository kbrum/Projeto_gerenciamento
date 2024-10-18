from scripts.Funcionalidades.Utils import *
from .Contas_a_pagar import *
from .Contas_a_receber import *
from .Saldo import *

class Financeiro: #Financeiro
    def name_app(): #titulo
        print('''
    ███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
    ██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
    █████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
    ██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
    ██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
    ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
              
    def mostrar_opcoes_financeiro(): #mostra as opções que o usuario pode escolher
        print('\n1 - Ver Saldo')
        print('2 - Contas a pagar')
        print('3 - Contas a receber')
        print('4 - Voltar ao menu inicial')

    def checagem_financeiro(): #faz a checagem doq foi escolhido entre os mostrados acima
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha = input('\n-------------> ').strip()
        
                # Verifica se a entrada está vazia
                if not escolha:
                    limpar_tela()
                    Financeiro.name_app()
                    Financeiro.mostrar_opcoes_financeiro()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)

                # Verifica as opções
                if escolha == 1:
                    limpar_tela()
                    Financeiro.name_app()
                    Saldo.mostrar_saldo()
                    Financeiro.executar_programa()
                    break

                elif escolha == 2:
                    limpar_tela()
                    Financeiro.name_app()
                    Contas_a_pagar.executar_programa()
                    Financeiro.executar_programa()
                    break
                
                elif escolha == 3:
                    limpar_tela()
                    Financeiro.name_app()
                    Contas_a_receber.executar_programa()
                    Financeiro.executar_programa()
                    break
                
                elif escolha == 4:
                    limpar_tela()
                    break
                
                else:
                    limpar_tela()
                    Financeiro.name_app()
                    Financeiro.mostrar_opcoes_financeiro()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Financeiro.name_app()
                Financeiro.mostrar_opcoes_financeiro()
                erro_de_valor()
        
    def executar_programa(): #executa todas as funções na ordem certa
        limpar_tela()
        Financeiro.name_app()
        Financeiro.mostrar_opcoes_financeiro()
        Financeiro.checagem_financeiro()
            
Financeiro.executar_programa() #usado para testes unitarios