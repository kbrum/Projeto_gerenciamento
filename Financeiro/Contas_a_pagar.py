from Funcionabilidades.Funções_basicas import Funções_basicas
from Funcionabilidades.Gerador_codigo import Codigo
from Funcionabilidades.Solicitações import Solicitar

class Nova_conta: #contrutor de uma nova conta
        def __init__(self,nome,tipo,dado,valor,codigo):
            self.nome = nome
            self.tipo = tipo
            self.dado = dado
            self.valor = valor
            self.codigo = codigo
            
class Contas_a_pagar:
    def name_app():
        print('''
    ░█████╗░░█████╗░███╗░░██╗████████╗░█████╗░░██████╗  ░█████╗░  ██████╗░░█████╗░░██████╗░░█████╗░██████╗░
    ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔════╝  ██╔══██╗  ██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗
    ██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░███████║╚█████╗░  ███████║  ██████╔╝███████║██║░░██╗░███████║██████╔╝
    ██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██║░╚═══██╗  ██╔══██║  ██╔═══╝░██╔══██║██║░░╚██╗██╔══██║██╔══██╗
    ╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║██████╔╝  ██║░░██║  ██║░░░░░██║░░██║╚██████╔╝██║░░██║██║░░██║
    ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝''')
        
        
    gerador = Codigo() #instacia do gerador de codigo

    lista_contas_a_pagar = [] #lista de contas a pagar
        
    def menu(): #pergunta ao usuario se quer voltar ao menu contas a pagar
        while True:
            try:
                Funções_basicas.limpar_tela()
                Contas_a_pagar.name_app()
                print('\nDeseja voltar ao menu contas a pagar? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Contas_a_pagar.name_app()
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
                    Contas_a_pagar.main_contas_a_pagar()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Contas_a_pagar.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')
    
    def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
        Funções_basicas.limpar_tela()
        Contas_a_pagar.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente a sua conta')
        print('\n Cadastro concluido com succeso')
        input('\n Pressione enter para continuar')
        
    def cadastrar_outra_conta(): #pergunta se quer cadastrar outra conta a pagar
        while True:
            try:
                Funções_basicas.limpar_tela()
                Contas_a_pagar.name_app()
                print('\nDeseja cadastrar outra conta?')
                print('1 - Sim')
                print('2 - Não')
                
                nv_produto = input('\n-------------> ').strip()
                
                if not nv_produto:
                    Funções_basicas.limpar_tela()
                    Contas_a_pagar.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                    
                nv_produto = int(nv_produto)
        
                if nv_produto == 1:
                    Funções_basicas.limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.cadastrar_conta()
                
                elif nv_produto == 2:
                    break
                
            except ValueError:
                Funções_basicas.limpar_tela()
                Contas_a_pagar.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def mostrar_contas(): # mostra as contas a pagar
        if len(Contas_a_pagar.lista_contas_a_pagar) == 0:
            print('\nNenhum produto cadastrado.')
        else:
            print('\nLista de produtos cadastrados:')
            for i, conta in enumerate(Contas_a_pagar.lista_contas_a_pagar, start=1):
                print(f'\n{i}. Nome: {conta.nome} | Tipo: {conta.tipo} |  CPF/CNPJ Do Recebedor: {conta.dado} |  Valor: {conta.valor} | Código: {conta.codigo}')
        
        input('\n(Digite Enter para continuar)')
        
    def cadastrar_conta(): #cadastra uma conta a pagar
        while True:
            try:
                nome = Solicitar.solicitar_entrada('Qual o nome da sua conta?', 'nome')
                tipo = Solicitar.solicitar_entrada('Qual o tipo da sua conta? (ex: Salário, Água, luz)', 'tipo')
                dado = Solicitar.solicitar_dados()
                valor = Solicitar.solicitar_valor_conta()
                codigo_conta = Contas_a_pagar.gerador.pro_num() 
                
                lista_conta = Nova_conta(nome,tipo,dado,valor,codigo_conta)
                
                Contas_a_pagar.lista_contas_a_pagar.append(lista_conta) #adciona uma nova conta a listade contas
                
                Contas_a_pagar.cadastro_feito()  # Confirma o cadastro da conta
                break 

            except ValueError:
                Funções_basicas.limpar_tela()
                Contas_a_pagar.name_app()
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
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.mostrar_opcoes()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)
   
                if escolha == 1:
                    Funções_basicas.limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.mostrar_contas()
                    Contas_a_pagar.menu()
                    break

                elif escolha == 2:
                    Funções_basicas.limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.cadastrar_conta()
                    Contas_a_pagar.cadastrar_outra_conta()
                    Contas_a_pagar.menu()
                    break
                
                elif escolha == 3:
                    break
                else:
                    Funções_basicas.limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.mostrar_opcoes()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                Funções_basicas.limpar_tela()
                Contas_a_pagar.name_app()
                Contas_a_pagar.mostrar_opcoes()
                Funções_basicas.erro_de_valor()

    def main_contas_a_pagar(): # agrupa e executa as funçoes do conta a pagar
        Funções_basicas.limpar_tela()
        Contas_a_pagar.name_app()
        Contas_a_pagar.mostrar_opcoes()
        Contas_a_pagar.checagem()
        
Contas_a_pagar.main_contas_a_pagar()
