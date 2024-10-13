import os

def preço_erro(): #erro de preço de produto
    print('\n Insira um Preço valido(APENAS NUMEROS)')

def erro_de_valor(): # aparece quando se digita algo que não é numero
    print('\nPor favor, selecione uma opção valida\n')

def limpar_tela(): # limpa a tela do terminal
    os.system('cls')
    
def cadastro_feito(quem_chama): #mostra mensagem de cadastro bem sucedido
        limpar_tela()
        quem_chama.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente')
        print('\n Cadastro concluido com succeso')
        input('\n Pressione enter para continuar')
    
def menu(quem_chama): #pergunta ao usuario se quer voltar ao menu de onde a função esta sendo chamada
        while True:
            try:
                limpar_tela()
                quem_chama.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    limpar_tela()
                    quem_chama.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de financeiro
                    limpar_tela()
                    quem_chama.main_quem_chama()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                limpar_tela()
                quem_chama.name_app()
                erro_de_valor()
                input('\n(Digite Enter para continuar)')
                
def cadastrar_outro(quem_chama): #pergunta se quer cadastrar outra coisa (conta, produto, funcionario)
        while True:
            try:    
                limpar_tela()
                quem_chama.name_app()
                print(f'\nDeseja cadastrar outro(a)?')
                print('1 - Sim')
                print('2 - Não')
                
                novo = input('\n-------------> ').strip()
                if not novo:
                    limpar_tela()
                    quem_chama.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                    
                novo = int(novo)
        
                if novo == 1:
                    limpar_tela()
                    quem_chama.name_app()
                    quem_chama.cadastrar_conta()
                
                elif novo == 2:
                    break
                
            except ValueError:
                limpar_tela()
                quem_chama.name_app()
                erro_de_valor()
                input('\n(Digite Enter para continuar)')
            
# Em "quem_chama" é colocado o nome da classe onde a função esta sendo chamada
