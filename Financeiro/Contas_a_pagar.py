from Funcionalidades.Utils import *
from Funcionalidades.Solicitações import *
from Funcionalidades.Gerador_codigo import *
from Funcionalidades.Construtores import Nova_conta
from datetime import datetime

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
        
    def mostrar_contas(): # mostra as contas a pagar
        if len(Contas_a_pagar.lista_contas_a_pagar) == 0:
            print('\nNenhum produto cadastrado.')
        else:
            print('\nLista de produtos cadastrados:')
            for i, conta in enumerate(Contas_a_pagar.lista_contas_a_pagar, start=1):
                status_conta = 'Pendente' if conta.status else 'Paga' # Fatora a string para exibir se a conta ja foi paga ou nao
                print(f'\n{i}. Nome: {conta.nome} | Tipo: {conta.tipo} |  CPF/CNPJ Do Recebedor: {conta.dado} |  Valor: R$ {conta.valor} | Data de abertura: {conta.data.strftime('%d/%m/%y')} | Código: {conta.codigo} | Status da conta: {status_conta}')
        
        input('\n(Digite Enter para continuar)')
        
    def cadastrar_conta(): #cadastra uma conta a pagar
        while True:
            try:
                nome = solicitar_entrada('Qual o nome da sua conta?', 'nome', Contas_a_pagar)
                tipo = solicitar_entrada('Qual o tipo da sua conta? (ex: Luz, Agua, Outros)', 'tipo', Contas_a_pagar)
                dado = solicitar_dados('Contas_a_pagar')                
                valor = solicitar_valor_conta()
                data = solicitar_data('Contas_a_pagar')
                codigo_conta = Contas_a_pagar.gerador.pro_num() 
                status = True
                
                lista_conta = Nova_conta(nome,tipo,dado,valor,data,codigo_conta,status)
                
                Contas_a_pagar.lista_contas_a_pagar.append(lista_conta) #adciona uma nova conta a listade contas
                
                cadastro_feito(Contas_a_pagar)  # Confirma o cadastro da conta
                break 

            except ValueError:
                limpar_tela()
                Contas_a_pagar.name_app()
                preço_erro()          

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
                    limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.mostrar_opcoes()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)
   
                if escolha == 1:
                    limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.mostrar_contas()
                    Contas_a_pagar.executar_programa()
                    break

                elif escolha == 2:
                    limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.cadastrar_conta()
                    cadastrar_outro(Contas_a_pagar)
                    Contas_a_pagar.executar_programa()
                    break
                
                elif escolha == 3:
                    break
                
                else:
                    limpar_tela()
                    Contas_a_pagar.name_app()
                    Contas_a_pagar.mostrar_opcoes()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Contas_a_pagar.name_app()
                Contas_a_pagar.mostrar_opcoes()
                erro_de_valor()

    def executar_programa(): # agrupa e executa as funçoes do conta a pagar
        limpar_tela()
        Contas_a_pagar.name_app()
        Contas_a_pagar.mostrar_opcoes()
        Contas_a_pagar.checagem()
        
#Contas_a_pagar.executar_programa() #para testes unitarios
