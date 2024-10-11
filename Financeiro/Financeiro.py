from Funcionabilidades.Funções_basicas import Funções_basicas
import Financeiro.Contas_a_pagar
class codigo: #gera um codigo de produto autoincrementavel
        def __init__(self):
            self.codigo = 0
            
        def pro_num(self):
            self.codigo +=1
            return self.codigo

class Financeiro: #Financeiro
    def name_app(): #titulo
        print('''
    ███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
    ██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
    █████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
    ██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
    ██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
    ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
        
    def menu_financeiro(): #pergunta ao usuario se quer voltar ao menu financeiro
        while True:
            try:
                Funções_basicas.limpar_tela()
                Financeiro.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
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
                    Financeiro.Principal.main_financeiro()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Financeiro.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')
    
    class Principal:
        
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
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.mostrar_opcoes_financeiro()
                        print('\nA escolha não pode ficar em branco.')
                        continue 

                    # Tenta converter para número inteiro
                    escolha = int(escolha)

                    # Verifica as opções
                    if escolha == 1:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Saldo.mostrar_saldo()
                        Financeiro.menu_financeiro()
                        break

                    elif escolha == 2:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_pagar.main_contas_a_pagar()
                        break
                    
                    elif escolha == 3:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_receber.main_contas_a_receber()
                        break
                    
                    elif escolha == 4:
                        Funções_basicas.limpar_tela()
                        Main.main()
                        break
                    
                    else:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Principal.mostrar_opcoes_financeiro()
                        print('Por favor, escolha uma opção válida.')

                except ValueError:  # Captura erros de conversão de string para int
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Financeiro.Principal.mostrar_opcoes_financeiro()
                    Funções_basicas.erro_de_valor()
            
        def main_financeiro(): #executa todas as funções na ordem certa
            Funções_basicas.limpar_tela()
            Financeiro.name_app()
            Financeiro.Principal.mostrar_opcoes_financeiro()
            Financeiro.Principal.checagem_financeiro()
            
        def executar_programa(): #mostra o programa na tela
            Financeiro.Principal.main_financeiro()
    
    class Saldo:
        saldo = 1000.00 #variavel que guarda o saldo
        def mostrar_saldo(): #mostra o saldo
            print(f'\n Seu saldo é de R$: {Saldo.saldo} ')
            input('\n Digite Enter para continuar')
            
    class Contas_a_pagar:
        contas_a_pagar = [] #lista do contas a pagar
         
        def menu(): #pergunta ao usuario se quer voltar ao menu contas a pagar
            while True:
                try:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    print('\nDeseja voltar ao menu contas a pagar? ')
                    print('1 - Sim')
                    print('2 - Não')
                    
                    menu = input('\n-------------> ').strip()
                    
                    if not menu: # verifica se a entrada do menu não é vazia
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
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
                        Financeiro.Contas_a_pagar.main_contas_a_pagar()
                        break
                    
                except ValueError: #em caso de inserir algo que não é numero na opção
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.erro_de_valor()
                    input('\n(Digite Enter para continuar)')
         
        def solicitar_dados():
            while True:
                try:
                    print('\nDigite o CPF ou CNPJ do recebedor')
                    dados = input('\n------------->').strip()
                    if len(dados) == 11:
                        dados = Financeiro.formatar_cpf(dados)
                        break
                    elif len(dados) == 14:
                        dados = Financeiro.formatar_cnpj(dados)
                        break
                    else:
                        raise ValueError("CPF/CNPJ inválido.")
                except ValueError as e:
                    print(f"\nErro: {e}. Não foi possível formatar o CPF/CNPJ.")
            
        def cadastrar_outra_conta(): #pergunta se quer cadastrar outra conta a pagar
            while True:
                try:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    print('\nDeseja cadastrar outra conta?')
                    print('1 - Sim')
                    print('2 - Não')
                    
                    nv_produto = input('\n-------------> ').strip()
                    
                    if not nv_produto:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        print('\nEste campo não pode ficar em branco')
                        input('\n(Digite Enter para continuar)')
                        continue
                        
                    nv_produto = int(nv_produto)
            
                    if nv_produto == 1:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_pagar.cadastrar_conta()
                    
                    elif nv_produto == 2:
                        break
                    
                except ValueError:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.erro_de_valor()
                    input('\n(Digite Enter para continuar)')

        def mostrar_contas(): # mostra as contas a pagar
            if len(Financeiro.Contas_a_pagar.contas_a_pagar) == 0:
                print('\nNenhum produto cadastrado.')
            else:
                print('\nLista de produtos cadastrados:')
                for i, conta in enumerate(Financeiro.Contas_a_pagar.contas_a_pagar, start=1):
                    print(f'\n{i}. Nome: {conta.nome} | Tipo: {conta.tipo} |  CPF/CNPJ Do Recebedor: {conta.dado} |  Valor: {conta.valor} | Código: {conta.codigo}')
            
            input('\n(Digite Enter para continuar)')
            
        
        def cadastrar_conta(): #cadastra uma conta a pagar
            while True:
                try:
                    nome = Financeiro.solicitar_entrada('Qual o nome da sua conta?', 'nome')
                    tipo = Financeiro.solicitar_entrada('Qual o tipo da sua conta? (ex: Salário, Água, luz)', 'tipo')
                    dados_recebedor = Financeiro.Contas_a_pagar.solicitar_dados()
                    valor = Financeiro.solicitar_valor()
                    
                    codigo_conta = Financeiro.gerador.pro_num() 
                    
                    lista_conta = Financeiro.conta(nome,tipo,dados_recebedor,valor,codigo_conta)
                    
                    Financeiro.Contas_a_pagar.contas_a_pagar.append(lista_conta)
                    
                    Financeiro.cadastro_feito()  # Confirma o cadastro da conta
                    break 

                except ValueError:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.preço_erro()          
    
        def mostrar_opcoes(): #mostra as opções que o usuario pode escolher no contas a pagar
            print('\n1 - Ver todas as contas a pagar')
            print('2 - Cadastrar contas')
            print('3 - Voltar ao menu financeiro')

        def checagem(): #faz a checagem doq foi no contas a pagar
            while True:
                try:
                    print('\nEscolha uma opção')
                    
                    # Captura a entrada e remove espaços em branco
                    escolha = input('\n-------------> ').strip()
            
                    # Verifica se a entrada está vazia
                    if not escolha:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_pagar.mostrar_opcoes()
                        print('\nA escolha não pode ficar em branco.')
                        continue 

                    # Tenta converter para número inteiro
                    escolha = int(escolha)

                    # Verifica as opções
                    if escolha == 1:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_pagar.mostrar_contas()
                        Financeiro.Contas_a_pagar.menu()
                        break

                    elif escolha == 2:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_pagar.cadastrar_conta()
                        Financeiro.Contas_a_pagar.cadastrar_outra_conta()
                        Financeiro.Contas_a_pagar.menu()
                        break
                    
                    elif escolha == 3:
                        Financeiro.Principal.main_financeiro()
                        break
                    else:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_pagar.mostrar_opcoes()
                        print('Por favor, escolha uma opção válida.')

                except ValueError:  # Captura erros de conversão de string para int
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Financeiro.Contas_a_pagar.mostrar_opcoes()
                    Funções_basicas.erro_de_valor()

        def main_contas_a_pagar(): # agrupa e executa as funçoes do conta a pagar
            Funções_basicas.limpar_tela()
            Financeiro.name_app()
            Financeiro.Contas_a_pagar.mostrar_opcoes()
            Financeiro.Contas_a_pagar.checagem()
    
    class Contas_a_receber:
        contas_a_receber = [] #lista de contas a receber

        def menu(): #pergunta ao usuario se quer voltar ao menu contas a pagar
            while True:
                try:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    print('\nDeseja voltar ao menu contas a receber? ')
                    print('1 - Sim')
                    print('2 - Não')
                    
                    menu = input('\n-------------> ').strip()
                    
                    if not menu: # verifica se a entrada do menu não é vazia
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
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
                        Financeiro.Contas_a_receber.main_contas_a_receber()
                        break
                    
                except ValueError: #em caso de inserir algo que não é numero na opção
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.erro_de_valor()
                    input('\n(Digite Enter para continuar)')
        
        def solicitar_dados():
            while True:
                try:
                    print('\nDigite o CPF ou CNPJ do pagante')
                    dados = input('\n------------->').strip()
                    if len(dados) == 11:
                        dados = Financeiro.formatar_cpf(dados)
                        break
                    elif len(dados) == 14:
                        dados = Financeiro.formatar_cnpj(dados)
                        break
                    else:
                        raise ValueError("CPF/CNPJ inválido.")
                except ValueError as e:
                    print(f"\nErro: {e}. Não foi possível formatar o CPF/CNPJ.")
        
        def cadastrar_outra_conta(): #pergunta se quer cadastrar outra conta a receber
            while True:
                try:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    print('\nDeseja cadastrar outra conta?')
                    print('1 - Sim')
                    print('2 - Não')
                    
                    nv_conta = input('\n-------------> ').strip()
                    
                    if not nv_conta:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        print('\nEste campo não pode ficar em branco')
                        input('\n(Digite Enter para continuar)')
                        continue
                        
                    nv_conta = int(nv_conta)
            
                    if nv_conta == 1:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_receber.cadastrar_conta()
                    
                    elif nv_conta == 2:
                        break
                    
                except ValueError:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.erro_de_valor()
                    input('\n(Digite Enter para continuar)')
        
        def cadastrar_conta(): #cadastra uma conta a receber
            while True:
                try:
                    nome = Financeiro.solicitar_entrada('Qual o nome da sua conta?', 'nome')
                    tipo = Financeiro.solicitar_entrada('Qual o tipo da sua conta? (ex: Salário, Contas mensais)', 'tipo')
                    dados_pagante = Financeiro.Contas_a_receber.solicitar_dados()
                    valor = Financeiro.solicitar_valor()
                    
                    codigo_conta = Financeiro.gerador.pro_num()

                    #armazena uma nova conta
                    lista_contas = Financeiro.conta(nome,tipo,dados_pagante,valor,codigo_conta)
                    
                    Financeiro.Contas_a_receber.contas_a_receber.append(lista_contas)
                    
                    Financeiro.cadastro_feito()  # Confirma o cadastro da conta
                    break 

                except ValueError:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.preço_erro()     

        def mostrar_contas(): # mostra as contas a pagar
            if len(Financeiro.Contas_a_receber.contas_a_pagar) == 0:
                print('\nNenhum produto cadastrado.')
            else:
                print('\nLista de produtos cadastrados:')
                for i, conta in enumerate(Financeiro.Contas_a_receber.contas_a_receber, start=1):
                    print(f'\n{i}. Nome: {conta.nome} | Tipo: {conta.tipo} |  CPF/CNPJ Do Pagante: {conta.dado} |  Valor: {conta.valor} | Código: {conta.codigo}')
            
            input('\n(Digite Enter para continuar)')

        def mostrar_opcoes(): #mostra as opções que o usuario pode escolher
            print('\n1 - Ver todas as contas a receber')
            print('2 - Cadastrar contas')
            print('3 - Voltar ao menu financeiro')

        def checagem(): #faz a checagem doq foi no contas a receber
            while True:
                try:
                    print('\nEscolha uma opção')
                    
                    # Captura a entrada e remove espaços em branco
                    escolha = input('\n-------------> ').strip()
            
                    # Verifica se a entrada está vazia
                    if not escolha:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_receber.mostrar_opcoes()
                        print('\nA escolha não pode ficar em branco.')
                        continue 

                    # Tenta converter para número inteiro
                    escolha = int(escolha)

                    # Verifica as opções
                    if escolha == 1:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_receber.mostrar_contas()
                        Financeiro.Contas_a_receber.menu()
                        break

                    elif escolha == 2:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_receber.cadastrar_conta()
                        Financeiro.Contas_a_receber.cadastrar_outra_conta()
                        Financeiro.Contas_a_receber.menu()
                        break
                    
                    elif escolha == 3:
                        Financeiro.Principal.main_financeiro()
                        break
                    else:
                        Funções_basicas.limpar_tela()
                        Financeiro.name_app()
                        Financeiro.Contas_a_receber.mostrar_opcoes()
                        print('Por favor, escolha uma opção válida.')

                except ValueError:  # Captura erros de conversão de string para int
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Financeiro.Contas_a_receber.mostrar_opcoes()
                    Funções_basicas.erro_de_valor()

        def main_contas_a_receber(): # agrupa e executa as funçoes do conta a pagar
            Funções_basicas.limpar_tela()
            Financeiro.name_app()
            Financeiro.mostrar_opcoes_contas_a_receber()
            Financeiro.checagem_contas_a_receber()


Financeiro.Principal.executar_programa() #usado para testes unitarios