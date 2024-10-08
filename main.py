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
    
def mostrar_opcoes():
    print('\nSeja bem vindo')
    print('\n1 - Produtos')
    print('2 - Estoque')
    print('3 - Financeiro')
    print('4 - Funcionarios')
    print('5 - Sair')

def checagem_main(): #Faz a checagem e autenticação da escolha
    while True:
        try:
            print('\nEscolha uma opção')
            
            # Captura a entrada e remove espaços em branco
            escolha_funcionario = input('\n-------------> ').strip()
    
            # Verifica se a entrada está vazia
            if not escolha_funcionario:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes()
                print('\nA escolha não pode ficar em branco.')
                continue 

            # Tenta converter para número inteiro
            escolha_funcionario = int(escolha_funcionario)

            # Verifica as opções
            if escolha_funcionario == 1:
                Funções_basicas.limpar_tela()
                name_app()
                Produtos.main_produtos()
                break

            elif escolha_funcionario == 2:
                Funções_basicas.limpar_tela()
                name_app()
                Estoque.main_estoque()
                break
            elif escolha_funcionario == 3:
                Funções_basicas.limpar_tela()
                name_app()
                Financeiro.main_financeiro()
                break
            
            elif escolha_funcionario == 4:
                Funções_basicas.limpar_tela()
                name_app()
                Funcionarios.main_funcionarios()
                break
            
            elif escolha_funcionario == 5:
                Funções_basicas.limpar_tela()
                name_app()
                confirmacao = input('\nTem certeza que deseja sair? (s/n): ').strip().lower()
                if confirmacao == 's':
                    Funções_basicas.limpar_tela()
                    print('\nFINALIZADO')
                    break
                else:
                    Funções_basicas.limpar_tela()
                    name_app()
                    mostrar_opcoes()
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes()
                print('Por favor, escolha uma opção válida.')

        except ValueError:  # Captura erros de conversão de string para int
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes()
            Funções_basicas.erro_de_valor()
    
def main():
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opcoes()
    checagem_main()
    
def executar_programa():#executa o programa 
    main()
    
executar_programa() #mostra na tela
