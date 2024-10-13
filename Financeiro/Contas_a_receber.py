from Funcionalidades import Funções_basicas 
from Funcionalidades import Gerador_codigo 
from Funcionalidades import Solicitações 

class Nova_conta: #contrutor de uma nova conta
        def __init__(self,nome,tipo,dado,valor,codigo):
            self.nome = nome
            self.tipo = tipo
            self.dado = dado
            self.valor = valor
            self.codigo = codigo
            
class Contas_a_receber:
    def name_app():
        print('''
    ░█████╗░░█████╗░███╗░░██╗████████╗░█████╗░░██████╗  ░█████╗░  ██████╗░███████╗░█████╗░███████╗██████╗░███████╗██████╗░
    ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔════╝  ██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗    
    ██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░███████║╚█████╗░  ███████║  ██████╔╝█████╗░░██║░░╚═╝█████╗░░██████╦╝█████╗░░██████╔
    ██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██║░╚═══██╗  ██╔══██║  ██╔══██╗██╔══╝░░██║░░██╗██╔══╝░░██╔══██╗██╔══╝░░██╔══██╗
    ╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║██████╔╝  ██║░░██║  ██║░░██║███████╗╚█████╔╝███████╗██████╦╝███████╗██║░░██║
    ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝  ╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝''')
        
    gerador = Gerador_codigo.Codigo() #instacia do gerador de codigo

    lista_Contas_a_receber = [] #lista de contas a pagar
        
    def menu(): #pergunta ao usuario se quer voltar ao menu contas a pagar
        while True:
            try:
                Funções_basicas.limpar_tela()
                Contas_a_receber.name_app()
                print('\nDeseja voltar ao menu contas a pagar? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Contas_a_receber.name_app()
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
                    Contas_a_receber.main_Contas_a_receber()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Contas_a_receber.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')
    
    def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
        Funções_basicas.limpar_tela()
        Contas_a_receber.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente a sua conta')
        print('\n Cadastro concluido com succeso')
        input('\n (Digite Enter para continuar)')
        
    def cadastrar_outra_conta(): #pergunta se quer cadastrar outra conta a pagar
        while True:
            try:
                Funções_basicas.limpar_tela()
                Contas_a_receber.name_app()
                print('\nDeseja cadastrar outra conta?')
                print('1 - Sim')
                print('2 - Não')
                
                nv_produto = input('\n-------------> ').strip()
                
                if not nv_produto:
                    Funções_basicas.limpar_tela()
                    Contas_a_receber.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                    
                nv_produto = int(nv_produto)
        
                if nv_produto == 1:
                    Funções_basicas.limpar_tela()
                    Contas_a_receber.name_app()
                    Contas_a_receber.cadastrar_conta()
                
                elif nv_produto == 2:
                    break
                
            except ValueError:
                Funções_basicas.limpar_tela()
                Contas_a_receber.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def mostrar_contas(): # mostra as contas a pagar
        if len(Contas_a_receber.lista_contas_a_receber) == 0:
            print('\nNenhum produto cadastrado.')
        else:
            print('\nLista de produtos cadastrados:')
            for i, conta in enumerate(Contas_a_receber.lista_contas_a_receber, start=1):
                print(f'\n{i}. Nome: {conta.nome} | Tipo: {conta.tipo} |  CPF/CNPJ Do Recebedor: {conta.dado} |  Valor: {conta.valor} | Código: {conta.codigo}')
        
        input('\n(Digite Enter para continuar)')
        
    def cadastrar_conta(): #cadastra uma conta a pagar
        while True:
            try:
                nome = Solicitações.solicitar_entrada('Qual o nome da sua conta?', 'nome')
                tipo = Solicitações.solicitar_entrada('Qual o tipo da sua conta? (ex: Salário, Água, luz)', 'tipo')
                dados_recebedor = Solicitações.solicitar_dados('Contas_a_receber')
                valor = Contas_a_receber.solicitar_valor()
                codigo_conta = Contas_a_receber.gerador.pro_num() 
                
                lista_conta = Nova_conta(nome,tipo,dados_recebedor,valor,codigo_conta)
                
                Contas_a_receber.lista_Contas_a_receber.append(lista_conta) #adciona uma nova conta a listade contas
                
                Contas_a_receber.cadastro_feito()  # Confirma o cadastro da conta
                break 

            except ValueError:
                Funções_basicas.limpar_tela()
                Contas_a_receber.name_app()
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
                    Contas_a_receber.name_app()
                    Contas_a_receber.mostrar_opcoes()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)

                if escolha == 1:
                    Funções_basicas.limpar_tela()
                    Contas_a_receber.name_app()
                    Contas_a_receber.mostrar_contas()
                    Contas_a_receber.menu()
                    break

                elif escolha == 2:
                    Funções_basicas.limpar_tela()
                    Contas_a_receber.name_app()
                    Contas_a_receber.cadastrar_conta()
                    Contas_a_receber.cadastrar_outra_conta()
                    Contas_a_receber.menu()
                    break
                
                elif escolha == 3:
                    break
                
                else:
                    Funções_basicas.limpar_tela()
                    Contas_a_receber.name_app()
                    Contas_a_receber.mostrar_opcoes()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                Funções_basicas.limpar_tela()
                Contas_a_receber.name_app()
                Contas_a_receber.mostrar_opcoes()
                Funções_basicas.erro_de_valor()

    def main_Contas_a_receber(): # agrupa e executa as funçoes do conta a pagar 
        Funções_basicas.limpar_tela()
        Contas_a_receber.name_app()   
        Contas_a_receber.mostrar_opcoes()