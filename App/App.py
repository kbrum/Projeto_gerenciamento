import sys
from Funcionalidades.Utils import *
from Funcionalidades.Geradorores import *
from Funcionalidades.Construtores import *
from Pedidos.Doces import *
from Pedidos.Salgados import *
from Pedidos.Controle import *
from Financeiro.Contas_a_pagar import *
from Financeiro.Contas_a_receber import *
from Financeiro.Saldo import *

class Produtos:
    def name_app():
        print('''
    ██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
    ██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
    ██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║░╚═══██╗
    ██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░''')
        
    gerador = Codigo()

    produtos = []

    def cadastrar_produto():  # Função para cadastrar um novo produto
        while True:
            try:
                nome = solicitar_entrada('Qual o nome do seu produto?', 'nome', Produtos).upper()
                tipo = solicitar_entrada('Qual o tipo do seu produto? (ex: Calçado, Vestuário, Eletrônico)', 'tipo', Produtos).upper()
                subsecao = solicitar_entrada('Qual a subseção do seu produto? (ex: Tenis, Camisa regata, Camisa social)', 'subseção', Produtos).upper()
                quantidade = solicitar_quantidade(Produtos)
                valor = solicitar_valor(Produtos,'Produtos')
                codigo_produto = Produtos.gerador.pro_num() 
                final = Novo_produto(nome,tipo,subsecao,quantidade,valor,codigo_produto)
                
                Produtos.produtos.append(final)
                
                cadastro_feito(Produtos)  # Confirma o cadastro do produto
                break 

            except ValueError:
                limpar_tela()
                Produtos.name_app()
                preço_erro()
                
    def mostrar_produtos():  # Função para mostrar todos os produtos cadastrados
        if len(Produtos.produtos) == 0:
            print('\nNenhum produto cadastrado.')
        else:
            print('\nLista de produtos cadastrados:')
            for i, produto in enumerate(Produtos.produtos, start=1):
                print(f'\n{i}. Nome: {produto.nome} | Tipo: {produto.tipo} | Subseção: {produto.subsecao} | Quantidade: {produto.quantidade} | Valor: R$ {produto.valor} | Código: {produto.codigo}')
            
        input('\n(Digite Enter para continuar)')
            
    def mostrar_opcoes(): #mostra as opções que o usuario pode escolher
        print('\n1 - Todos os produtos')
        print('2 - Cadastrar produto')
        print('3 - Voltar ao menu')
        
    def checagem(): #faz a checagem doq foi escolhido entre os mostrados acima
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha = input('\n-------------> ').strip()
        
                # Verifica se a entrada está vazia
                if not escolha:
                    limpar_tela()
                    Produtos.name_app()
                    Produtos.mostrar_opcoes_produtos()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)

                # Verifica as opções
                if escolha == 1:
                    limpar_tela()
                    Produtos.name_app()
                    Produtos.mostrar_produtos()
                    Produtos.executar_programa()
                    break

                elif escolha == 2:
                    limpar_tela()
                    Produtos.cadastrar_produto()
                    cadastrar_outro(Produtos)
                    Produtos.executar_programa()
                    break
                
                elif escolha == 3:
                    limpar_tela()
                    break
                
                else:
                    limpar_tela()
                    Produtos.name_app()
                    Produtos.mostrar_opcoes_produtos()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Produtos.name_app()
                Produtos.mostrar_opcoes_produtos()
                erro_de_valor()

    def executar_programa():#mostra o programa na tela
        limpar_tela()
        Produtos.name_app()
        Produtos.mostrar_opcoes()
        Produtos.checagem()

class Pedidos: #Pedidos
    def name_app():
        print('''
    ██████╗░███████╗██████╗░██╗██████╗░░█████╗░░██████╗
    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████╗░░██║░░██║██║██║░░██║██║░░██║╚█████╗░
    ██╔═══╝░██╔══╝░░██║░░██║██║██║░░██║██║░░██║░╚═══██╗
    ██║░░░░░███████╗██████╔╝██║██████╔╝╚█████╔╝██████╔╝
    ╚═╝░░░░░╚══════╝╚═════╝░╚═╝╚═════╝░░╚════╝░╚═════╝░''')
    
    def mostrar_opcoes(): # mostra as oções que podem ser escolhidas
        print('\n1 - Seção de doces')
        print('2 - Seção de salgados')
        print('3 - Fazer pedido')
        print('4 - Voltar ao menu principal')

    def checagem(): # checa a opção q o usuario escolheu
        while True:
            try:
                print('\nEscolha uma opção')
                escolha = int(input('\n-------------> '))
                
                if escolha == 1:
                    limpar_tela()
                    Doces.executar_programa()
                    Pedidos.executar_programa()                  
                    break
                
                elif escolha == 2:
                    limpar_tela()
                    Salgados.executar_programa()
                    Pedidos.executar_programa() 
                    break
                
                elif escolha== 3:
                    limpar_tela()
                    Controle_pedido.fazer_pedido(Pedidos, 'Pedidos')
                    Pedidos.executar_programa()
                    break                
                
                elif escolha == 4:
                    limpar_tela()
                    break
            
            except ValueError:
                limpar_tela()
                Pedidos.name_app()
                Pedidos.mostrar_opcoes()
                erro_de_valor()
                Pedidos.checagem()
            
    def executar_programa(): # mostra na tela
        limpar_tela()
        Pedidos.name_app()
        Pedidos.mostrar_opcoes()
        Pedidos.checagem()

from Funcionalidades.Utils import *

class Estoque:
    def name_app(): # titulo    
        print('''
    ███████╗░██████╗████████╗░█████╗░░██████╗░██╗░░░██╗███████╗
    ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██║░░░██║██╔════╝
    █████╗░░╚█████╗░░░░██║░░░██║░░██║██║██╗██║██║░░░██║█████╗░░
    ██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║╚██████╔╝██║░░░██║██╔══╝░░
    ███████╗██████╔╝░░░██║░░░╚█████╔╝░╚═██╔═╝░╚██████╔╝███████╗
    ╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝''')

    em_falta = [] #lista de produtos em falta
    produtos_em_estoque = [] #todos os produtos

    def Em_falta():#mostra os produtos em falta
        if Estoque.em_falta:
            print('\nOs produtos em falta são:')
            for produtos_em_falta in Estoque.em_falta:
                print(f'.{produtos_em_falta}')
        else:
            limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
                
    def mostra_estoque(): #mostra todo o estoque
        if Estoque.produtos_em_estoque:
            print('\nProdutos em estoque:')
            for produtos in Estoque.produtos_em_estoque:
                print(f'.{produtos}')
        else:
            limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
            
    def mostrar_opcoes_estoque(): #mostra a opções q o usuario pode escolher
        print('\n1 - Ver todos')
        print('2 - Em falta')
        print('3 - Voltar ao menu inicial')

    def checagem_estoque(): #faz a checagem doq foi escolhido entre os mostrados acima
        while True:
            try:
                print('\nEscolha uma opção')
                
                escolha = input('\n-------------> ').strip()
                
                if not escolha:
                    limpar_tela()
                    Estoque.name_app()
                    Estoque.mostrar_opcoes_estoque()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)
                
                if escolha == 1:
                    limpar_tela()
                    Estoque.name_app()
                    Estoque.mostra_estoque()
                    Estoque.executar_programa()    
                    break
                
                elif escolha == 2:
                    limpar_tela()
                    Estoque.name_app()
                    Estoque.Em_falta()
                    Estoque.executar_programa()
                    break
                
                elif escolha == 3:
                    limpar_tela()
                    break
            
            except:
                limpar_tela()
                Estoque.name_app()
                Estoque.mostrar_opcoes_estoque()
                erro_de_valor()
        
    def main_estoque(): #executa todas as funções na ordem certa
        limpar_tela()
        Estoque.name_app()
        Estoque.mostrar_opcoes_estoque()
        Estoque.checagem_estoque()
        
    def executar_programa(): #mostra o programa na tela
        Estoque.main_estoque()

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

class Funcionarios: #Funcionarios
    def name_app():
        print('''
    ███████╗░██████╗░██╗░░░██╗██╗██████╗░███████╗
    ██╔════╝██╔═══██╗██║░░░██║██║██╔══██╗██╔════╝
    █████╗░░██║██╗██║██║░░░██║██║██████╔╝█████╗░░
    ██╔══╝░░╚██████╔╝██║░░░██║██║██╔═══╝░██╔══╝░░
    ███████╗░╚═██╔═╝░╚██████╔╝██║██║░░░░░███████╗
    ╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝╚═╝░░░░░╚══════╝''')

    gerador = Codigo() #instacia do gerador de codigo

    lista_funcionarios = []

    def cadastrar_funcionario():  # Função para cadastrar um novo funcionário
        while True:
            try:
                nome = solicitar_entrada('Qual o nome do seu funcionario?', 'nome', Funcionarios).upper()
                setor = solicitar_entrada('Qual o setor do seu funcionario?', 'setor', Funcionarios).upper()
                posicao = solicitar_entrada('Qual a posição desse funcionario? (ex: Analista, Tecnico, Estagiarios)', 'posição', Funcionarios)
                codigo = Funcionarios.gerador.pro_num()
                status = True
                
                # Armazena o novo funcionário
                funcionario_di = Novo_funcionario(nome,setor,posicao,codigo,status)
                Funcionarios.lista_funcionarios.append(funcionario_di)

                cadastro_feito(Funcionarios)  # Função para notificar que o cadastro foi feito
                break

            except Exception as e:
                limpar_tela()
                Funcionarios.name_app()
                print(f'\nErro: {e}')
                print('\nEste campo não pode ficar em branco.')

    def mostrar_funcionarios():  # Função para mostrar os funcionários cadastrados
        if len(Funcionarios.lista_funcionarios) == 0:
            print('\nNenhum funcioanrio cadastrado.')
        
        else:
            print('\nSeus funcionários são:')
            for funcionario in Funcionarios.lista_funcionarios:
                status_funcionarios = 'Ativo' if funcionario.status else 'desligado'    
                print(f'\n--> Nome: {funcionario.nome} | Setor: {funcionario.setor} | Posição: {funcionario.posicao} | Código: {funcionario.codigo} | Status do contrato: {status_funcionarios}')
            input('\n(Digite Enter para continuar)')

    def mostrar_opcoes(): #mostra as opçoes que o usuario pode escolher
        print('\n1 - Todos os funcionarios')
        print('2 - Cadastrar funcionario')
        print('3 - Voltar ao menu principal')

    def checagem():  # Checa a escolha que o usuário fez
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha = input('\n-------------> ').strip()

                # Verifica se a entrada está vazia
                if not escolha:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.mostrar_opcoes_funcionarios()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)

                # Verifica as opções
                if escolha == 1:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.mostrar_funcionarios()
                    Funcionarios.executar_programa()
                    break

                elif escolha == 2:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.cadastrar_funcionario()
                    cadastrar_outro(Funcionarios)
                    Funcionarios.executar_programa()
                    break
                
                else:
                    limpar_tela()
                    break

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Funcionarios.name_app()
                Funcionarios.mostrar_opcoes()
                erro_de_valor()     
        
    def executar_programa(): #executa o programa
        limpar_tela()
        Funcionarios.name_app()
        Funcionarios.mostrar_opcoes()
        Funcionarios.checagem()

class Main: #MAIN.
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
        print('2 - Pedidos')
        print('3 - Estoque')
        print('4 - Financeiro')
        print('5 - Funcionarios')
        print('6 - Sair')

    def checagem(): #Faz a checagem e autenticação da escolha
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha = input('\n-------------> ').strip()
        
                # Verifica se a entrada está vazia
                if not escolha:
                    limpar_tela()
                    Main.name_app()
                    Main.mostrar_opcoes()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)
                
                # Verifica as opções
                if escolha == 1:
                    Produtos.executar_programa()
                    Main.executar_programa()
                    break
                
                elif escolha == 2:
                    Pedidos.executar_programa()
                    Main.executar_programa()
                    break
                elif escolha == 3:
                    Estoque.executar_programa()
                    Main.executar_programa()
                    break
                
                elif escolha == 4:
                    Financeiro.executar_programa()
                    Main.executar_programa()
                    break
                
                elif escolha == 5:
                    Funcionarios.executar_programa()
                    Main.executar_programa()
                    break
                
                elif escolha == 6:
                    limpar_tela()
                    print('FINALIZADO')
                    sys.exit()
                
                else:
                    limpar_tela()
                    Main.name_app()
                    Main.mostrar_opcoes()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Main.name_app()
                Main.mostrar_opcoes()
                erro_de_valor()    
        
    def executar_programa():#executa o programa 
        limpar_tela()
        Main.name_app()
        Main.mostrar_opcoes()
        Main.checagem()
        
Main.executar_programa()# mostra o programa na tela 