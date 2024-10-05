import Produtos
import Financeiro
import Funcionarios
import Estoque
import Funções_basicas

def name_app():     
    print('''
░██████╗░███████╗██████╗░███████╗███╗░░██╗░█████╗░██╗░█████╗░
██╔════╝░██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██║██╔══██╗
██║░░██╗░█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝██║███████║
██║░░╚██╗██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██║██╔══██║
╚██████╔╝███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚═╝''')
    
def exibir_opcoes():
    print('\nSeja bem vindo')
    print('\n1 - Produtos')
    print('2 - Estoque')
    print('3 - Financeiro')
    print('4 - Funcionarios')
    print('5 - Sair')

def Conferir_alternativas(): #Faz a checagem e autenticação da escolha
    while True:
        try:
            escolha = int(input('\nEscolha uma opção: '))
                    
            if escolha == 1:
                Funções_basicas.limpar_tela()
                Produtos.main_produtos()
                break
                        
            elif escolha == 2:
                Funções_basicas.limpar_tela()
                Estoque.main_estoque()
                break
            
            elif escolha == 3:
                Funções_basicas.limpar_tela()
                Financeiro.main_financeiro()
                break
                        
            elif escolha == 4:
                Funções_basicas.limpar_tela()
                Funcionarios.main_funcionarios()
                break
                        
            elif escolha == 5:
                Funções_basicas.limpar_tela()
                print('Finalizado')
                break
                    
            else:
                Funções_basicas.erro_de_valor()
        except:
            Funções_basicas.erro_de_valor()
        
def main():
    Funções_basicas.limpar_tela()
    name_app()
    exibir_opcoes()
    Conferir_alternativas()
    
    
main()