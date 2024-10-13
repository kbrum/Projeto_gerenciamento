import sys
from Funcionalidades.Utils import *
from Funcionalidades.Gerador_codigo import *
from Financeiro.Contas_a_pagar import *
from Financeiro.Contas_a_receber import *
from Financeiro.Saldo import *

class Produtos:
    def name_app():
        print('''
    ██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
    ██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
    ██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░ ░░██║░░██║░╚═══██╗
    ██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░''')
        
    class Produto:
        def __init__(self,nome,tipo,subsecao,quantidade,preço,codigo):
            self.nome = nome
            self.tipo = tipo
            self.subsecao = subsecao
            self.quantidade = quantidade
            self.preço = preço
            self.codigo = codigo
    
    gerador = Codigo() #instacia do gerador de codigo

    def menu_produtos(): #pergunta ao usuario se quer voltar ao menu 
        while True:
                try:
                    limpar_tela()
                    Produtos.name_app()
                    print('\nDeseja voltar ao menu? ')
                    print('1 - Sim')
                    print('2 - Não')
                    
                    menu = input('\n-------------> ').strip()
                    
                    if not menu: # verifica se a entrada do menu não é vazia
                        limpar_tela()
                        Produtos.name_app()
                        print('\nEste campo não pode ficar em branco')
                        input('\n(Digite Enter para continuar)')
                        continue
                    
                    menu = int(menu)
                    
                    if menu == 2: # fecha o programa
                        limpar_tela()
                        print('Finalizado')
                        break
                    
                    elif menu == 1: # volta ao menu de produtos
                        limpar_tela()
                        Produtos.main_produtos()
                        break
                    
                except ValueError: #em caso de inserir algo que não é numero na opção
                    limpar_tela()
                    Produtos.name_app()
                    erro_de_valor()
                    input('\n(Digite Enter para continuar)')

    def cadastrar_outro_produto(): #pergunta se quer cadastrar outro produto
        while True:
            try:
                limpar_tela()
                Produtos.name_app()
                print('\nDeseja cadastrar outro produto?')
                print('1 - Sim')
                print('2 - Não')
                
                nv_produto = input('\n-------------> ').strip()
                
                if not nv_produto:
                    limpar_tela()
                    Produtos.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                    
                nv_produto = int(nv_produto)
        
                if nv_produto == 1:
                    limpar_tela()
                    Produtos.name_app()
                    Produtos.cadastrar_produto()
                
                elif nv_produto == 2:
                    break
                
            except ValueError:
                limpar_tela()
                Produtos.name_app()
                erro_de_valor()
                input('\n(Digite Enter para continuar)')

    produtos = []

    def solicitar_preco():  # Função para garantir que o preço seja numérico e positivo
        while True:
            try:
                print('\nQual o preço do seu produto? (Insira apenas números)')
                preço = float(input('\n------------->').strip())
                if preço > 0:
                    return preço
                else:
                    limpar_tela()
                    Produtos.name_app()
                    print('O preço do produto deve ser positivo.')
            except ValueError:
                limpar_tela()
                Produtos.name_app()
                preço_erro()

    def solicitar_quantidade(): #solicita a quantidade de produtos em estoque
        while True:
            try:
                print('\nQual a quantidade do seu produto? (Insira apenas números)')
                preço = int(input('\n------------->').strip())
                if preço > 0:
                    return preço
                else:
                    limpar_tela()
                    Produtos.name_app()
                    print('A quantidade do produto deve ser positiva.')
            except ValueError:
                limpar_tela()
                Produtos.name_app()
                preço_erro()
        
    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                limpar_tela()
                Produtos.name_app()
                print(f'\nA parte de {tipo} do seu produto não pode ficar em branco.')

    def cadastrar_produto():  # Função para cadastrar um novo produto
        while True:
            try:
                nome = Produtos.solicitar_entrada('Qual o nome do seu produto?', 'nome')
                tipo = Produtos.solicitar_entrada('Qual o tipo do seu produto? (ex: Calçado, Vestuário, Eletrônico)', 'tipo')
                subsecao = Produtos.solicitar_entrada('Qual a subseção do seu produto? (ex: Tenis, Camisa regata, Camisa social)', 'subseção')
                quantidade = Produtos.solicitar_quantidade()
                preço = Produtos.solicitar_preco()
                
                codigo_produto = Produtos.gerador.pro_num()  # Substitua por sua função geradora de código
                
                final = Produtos.Produto(nome,tipo,subsecao,quantidade,preço,codigo_produto)
                
                Produtos.produtos.append(final)
                
                Produtos.cadastro_feito()  # Confirma o cadastro do produto
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
                print(f'{i}. Nome: {produto.nome} | Tipo: {produto.tipo} | Subseção: {produto.subsecao} | Quantidade: {produto.quantidade} | Preço: {produto.preço} | Código: {produto.codigo}')
            
        input('\n(Digite Enter para continuar)')
            
    def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
        limpar_tela()
        Produtos.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente a seu produto')
        print('\n Cadastro concluido com succeso')
        input('\n Pressione enter para continuar')
            
    def mostrar_opcoes_produtos(): #mostra as opções que o usuario pode escolher
        print('\n1 - Todos os produtos')
        print('2 - Cadastrar produto')
        print('3 - Voltar ao menu')
        
    def checagem_produtos(): #faz a checagem doq foi escolhido entre os mostrados acima
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
                    Produtos.menu_produtos()
                    break

                elif escolha == 2:
                    limpar_tela()
                    Produtos.name_app()
                    Produtos.cadastrar_produto()
                    Produtos.cadastrar_outro_produto()
                    Produtos.menu_produtos()
                    break
                
                elif escolha == 3:
                    limpar_tela()
                    Main.main()
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
        
    def main_produtos(): #executa todas as funções na ordem certa
        limpar_tela()
        Produtos.name_app()
        Produtos.mostrar_opcoes_produtos()
        Produtos.checagem_produtos()

    def executar_programa():#mostra o programa na tela
        Produtos.main_produtos()

class Pedidos: #Pedidos
    def name_app():
        print('''
    ██████╗░███████╗██████╗░██╗██████╗░░█████╗░░██████╗
    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████╗░░██║░░██║██║██║░░██║██║░░██║╚█████╗░
    ██╔═══╝░██╔══╝░░██║░░██║██║██║░░██║██║░░██║░╚═══██╗
    ██║░░░░░███████╗██████╔╝██║██████╔╝╚█████╔╝██████╔╝
    ╚═╝░░░░░╚══════╝╚═════╝░╚═╝╚═════╝░░╚════╝░╚═════╝░         
              ''')
        
    class Pedido: #obejto pedido
        def __init__(self,nome,tipo,quantidade,contato,valor,pagamento,codigo,status): #construtor de um novo pedido
            self.nome = nome
            self.tipo = tipo
            self.quantidade = quantidade
            self.contato = contato
            self.valor = valor
            self.pagamento = pagamento
            self.codigo = codigo
            self.status = status
        
        def finalizar_pedido(self): # finalizador de pedidos (altera o self.status de true para false ('pedido ativo/pedido finalizado'))
            if self.status:  # Verifica se o pedido está ativo
                self.status = False
                print(f"Pedido {self.codigo} finalizado.")
            else:
                print(f"Pedido {self.codigo} já está finalizado.")
        
    gerador = Codigo() #instacia do gerador de codigo
    
    class FazerPedido: # para fazer um novo pedido
        
        def solicitar_valor():  # Função para garantir que o preço seja numérico
            while True:
                try:
                    print('\nQual o valor do seu pedido? (Insira apenas números)')
                    valor = float(input('\n------------->').strip())
                    if valor > 0:
                        return valor
                    else:
                        limpar_tela()
                        Pedidos.name_app()
                        print('O valor do pedido deve ser positivo.')
                except ValueError:
                    limpar_tela()
                    Pedidos.name_app()
                    preço_erro()
        
        def solicitar_pagamento(): #Pergunta a forma de pagamento
            while True:
                try:
                    limpar_tela()
                    Pedidos.name_app()
                    print('\nQual a forma de pagamento? ')
                    print('1 - Cartão de Débito')
                    print('2 - Cartão de Crédito')
                    print('3 - Pix')
                    
                    pagamento = input('\n-------------> ').strip()
                    
                    if not pagamento: # verifica se a entrada do pagamento não é vazia
                        limpar_tela()
                        Pedidos.name_app()
                        print('\nEste campo não pode ficar em branco')
                        input('\n(Digite Enter para continuar)')
                        continue
                    
                    pagamento = int(pagamento)
                    
                    if pagamento == 1: # pagar com debito
                        limpar_tela()
                        pagamento = 'Cartão de Débito'
                        break
                    
                    elif pagamento == 2: # pagar com credito
                        limpar_tela()
                        pagamento = 'Cartão Crédito'
                        break
                    
                    elif pagamento == 3: # pagar com pix
                        limpar_tela()
                        pagamento = 'Pix'
                        break
                    
                except ValueError: #em caso de inserir algo que não é numero na opção
                    limpar_tela()
                    Pedidos.name_app()
                    erro_de_valor()
                    input('\n(Digite Enter para continuar)')
 
            return pagamento

        def solicitar_quantidade(): #solicita a quantidade de produtos em estoque
            while True:
                try:
                    print('\nQual a quantidade de itens no pedido? (Insira apenas números)')
                    preço = int(input('\n------------->').strip())
                    if preço > 0:
                        return preço
                    else:
                        limpar_tela()
                        Pedidos.name_app()
                        print('A quantidade do produto deve ser positiva.')
                except ValueError:
                    limpar_tela()
                    Pedidos.name_app()
                    preço_erro()
    
        def solicitar_numero(): # solicta um numero para contato
                while True:
                    try:
                        print('\nDigite um numero para contato (com DDD)')
                        numero = input('\n------------->').strip()
                        if len(numero) == 11:
                            numero = Pedidos.formatar_numero(numero)
                            break
                        else:
                            raise ValueError("Numero inválido.")
                    except ValueError as e:
                        print(f"\nErro: {e}. Não foi possível formatar o numero.")
                
                return numero
            
        def pedido_feito(): #mostra mensagem de pedido bem sucedido
            limpar_tela()
            Pedidos.name_app()
            print('\n Um codigo de identificação foi gerado automaticamente a seu Pedido')
            print('\n Pedido realizado com succeso')
            input('\n Pressione enter para continuar')
        
        pedidos = []
    
        def cadastrar_pedido():  # Função para cadastrar um novo produto
            while True:
                try:
                    nome = Pedidos.solicitar_entrada('Qual o nome de quem esta fazendo o pedido', 'nome')
                    tipo = Pedidos.solicitar_entrada('Qual o tipo do seu pedido? (ex: Bolo, Doces, Torta)', 'tipo')
                    quantidade = Pedidos.FazerPedido.solicitar_quantidade()
                    numero = Pedidos.FazerPedido.solicitar_numero()
                    valor = Pedidos.FazerPedido.solicitar_valor()
                    pagamento = Pedidos.FazerPedido.solicitar_pagamento()
                    codigo = Pedidos.gerador.pro_num()
                    status = True
                    
                    final = Pedidos.Pedido(nome,tipo,quantidade,numero,valor,pagamento,codigo,status)
                    
                    Pedidos.FazerPedido.pedidos.append(final)
                    
                    Pedidos.FazerPedido.pedido_feito()  # Confirma o cadastro do produto
                    break 

                except ValueError:
                    limpar_tela()
                    Pedidos.name_app()
                    preço_erro()
                           
    def menu_pedidos(): #pergunta ao usuario se quer voltar ao menu financeiro
        while True:
            try:
                limpar_tela()
                Pedidos.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    limpar_tela()
                    Pedidos.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de pedidos
                    limpar_tela()
                    Pedidos.main_pedidos()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                limpar_tela()
                Pedidos.name_app()
                erro_de_valor()
                input('\n(Digite Enter para continuar)')
    
    def formatar_numero(numero): #formata um numero
        numero = ''.join(filter(str.isdigit, numero))  # Remove qualquer caractere que não seja dígito
        if len(numero) != 11:
            raise ValueError("O numero deve ter 11 dígitos.")
        return f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'
    
    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                limpar_tela()
                Pedidos.name_app()
                print(f'\nO {tipo} do seu produto não pode ficar em branco.')  
    
    def mostrar_todos(): #mostra todos os pedidos ja feitos
        if len(Pedidos.FazerPedido.pedidos) == 0: # checa se a lista esta vazia
            print('\nNenhum pedido cadastrado.')
        else:
            print('\nLista de pedidos feitos:')
            for i, pedido in enumerate(Pedidos.FazerPedido.pedidos, start=1):
                status_pedido = 'Pedido ativo' if pedido.status else 'Pedido finalizado' # Fatora a string para exibir pedido ativo ou finalizado em vez de true ou false
                print(f'\n{i}. Nome: {pedido.nome} | Tipo: {pedido.tipo} | Quantidade: {pedido.quantidade} | Numero para contato: {pedido.contato} | Valor do pedido: R${pedido.valor} | Forma de pagamento: {pedido.pagamento} | Código: {pedido.codigo} | Status do pedido: {status_pedido}')
                #exibe na tela os pedidos
                
        input('\n(Digite Enter para continuar)')
    
    def mostrar_ativos(): #mostra apenas os pedidos ativos
        if len(Pedidos.FazerPedido.pedidos) == 0:
            print('\nNenhum pedido ativo ou cadastrado')
        else:
            print('\nLista de pedidos feitos:')
            for i, pedido in enumerate(Pedidos.FazerPedido.pedidos, start=1):
                status_pedido = 'Pedido ativo' if pedido.status else 'Pedido finalizado' # Fatora a string para exibir pedido ativo ou finalizado em vez de true ou false
                if status_pedido == 'Pedido ativo': # verifica se o pedido esta ativo ou finalizado
                    print(f'\n{i}. Nome: {pedido.nome} | Tipo: {pedido.tipo} | Quantidade: {pedido.quantidade} | Numero para contato: {pedido.contato} | Valor do pedido: R${pedido.valor} | Forma de pagamento: {pedido.pagamento} | Código: {pedido.codigo} | Status do pedido: {status_pedido}')
                else:
                    print('\nNenhum pedido ativo ou cadastrado')  

        input('\n(Digite Enter para continuar)')
        
    def alterar_status_pedido(): # Solicita ao usuário o código do pedido para finalizar
        while True:
            try:
                limpar_tela()
                Pedidos.name_app()
                codigo = int(input('Digite o código do pedido que deseja finalizar: ').strip())
                
                # Busca o pedido com o código informado
                pedido_encontrado = None # gera uma variavel fazia para procurar o codigo na lista
                for pedido in Pedidos.FazerPedido.pedidos: # procurando o codigo na lista
                    if pedido.codigo == codigo:
                        pedido_encontrado = pedido # caso ele exista ele é alocado dentro da variavel 'pedido_encontrado'
                
                if pedido_encontrado:
                    pedido_encontrado.finalizar_pedido() # chama a função que finaliza pedidos
                    
                    print('\nStatus dos pedidos após alteração:') #informa que o pedido x foi finalizado com sucesso
                    for pedido in Pedidos.FazerPedido.pedidos:
                        limpar_tela()
                        Pedidos.name_app()
                        print(f'\nO pedido de código {pedido.codigo} foi {'Ativo' if pedido.status else 'Finalizado'} com sucesso') # mensagem de finalizado
                        
                    input('\n(Precione Enter para continuar)')
                    break
                
                else:
                    print(f'\nPedido com código {codigo} não encontrado.') #caso o pedido não seja encontrado
            
            except ValueError:
                print('Erro: O código do pedido deve ser um número inteiro.') # caso digite uma letra ou deixe vazio
  
    def mostrar_opcoes(): # mostra as oções que podem ser escolhidas
        print('\n1 - Ver todos os pedidos')
        print('2 - Ver pedidos ativos')
        print('3 - Fazer pedido')
        print('4 - Finalizar pedido')
        print('5 - Voltar ao menu principal')
    
    def checagem(): # checa a opção q o usuario escolheu
        while True:
            try:
                print('\nEscolha uma opção')
                escolha = int(input('\n-------------> '))
                
                if escolha == 1:
                    limpar_tela()
                    Pedidos.name_app()
                    Pedidos.mostrar_todos()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha == 2:
                    limpar_tela()
                    Pedidos.name_app()
                    Pedidos.mostrar_ativos()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha== 3:
                    limpar_tela()
                    Pedidos.name_app()
                    Pedidos.FazerPedido.cadastrar_pedido()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha == 4:
                    limpar_tela()
                    Pedidos.name_app()
                    Pedidos.alterar_status_pedido()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha == 5:
                    limpar_tela()
                    Main.main()
                    break
            
            except ValueError:
                limpar_tela()
                Pedidos.name_app()
                Pedidos.mostrar_opcoes()
                erro_de_valor()
                Pedidos.checagem()
    
    def main_pedidos(): # executa as funçoes na ordem
        limpar_tela()
        Pedidos.name_app()
        Pedidos.mostrar_opcoes()
        Pedidos.checagem()
        
    def executar_programa(): # mostra na tela
        Pedidos.main_pedidos()

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
                    Estoque.Produtos_em_falta()
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
        
    def menu_funcionacios(): #pergunta ao usuario se quer voltar ao menu 
        while True:
            try:
                limpar_tela()
                Funcionarios.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    limpar_tela()
                    Funcionarios.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de funcionarios
                    limpar_tela()
                    Funcionarios.main_funcionarios()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                limpar_tela()
                Funcionarios.name_app()
                erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def cadastrar_outro_funcionario(): #pergunta se quer cadastrar outro funcionario
        while True:
            try:
                limpar_tela()
                Funcionarios.name_app()
                print('\nDeseja cadastrar outro funcionario')
                print('1 - Sim')
                print('2 - Não')
                nv_funcionario = int(input('\n------------->'))
        
                if nv_funcionario == 1:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.cadastrar_funcionario()
                
                elif nv_funcionario == 2:
                    break
                
            except:
                limpar_tela()
                Funcionarios.name_app()
                erro_de_valor()
                Funcionarios.cadastrar_outro_funcionario()
                break

    def solicitar_entrada(mensagem, setor):  # Função para garantir que a entrada não esteja em branco
        while True:
            entrada = input(f'\n{mensagem}\n------------->').strip()
            if entrada:
                return entrada
            else:
                limpar_tela()
                Funcionarios.name_app()
                print(f'\nO {setor} do seu funcionario não pode ficar em branco.')

    funcionarios = []

    def cadastrar_funcionario():  # Função para cadastrar um novo funcionário
        while True:
            try:
                nome = Funcionarios.solicitar_entrada('Qual o nome do seu funcionario?', 'nome')
                setor = Funcionarios.solicitar_entrada('Qual o setor do seu funcionario?', 'setor')

                codigo_funcionario = Funcionarios.gerador.pro_num()

                # Armazena o novo funcionário
                funcionario_di = {
                    'nome': nome,
                    'setor': setor,
                    'codigo_funcionario': codigo_funcionario}
                
                Funcionarios.funcionarios.append(funcionario_di)

                Funcionarios.cadastro_feito()  # Função para notificar que o cadastro foi feito
                break

            except Exception as e:
                limpar_tela()
                Funcionarios.name_app()
                print(f'\nErro: {e}')
                print('\nEste campo não pode ficar em branco.')

    def mostrar_funcionarios():  # Função para mostrar os funcionários cadastrados
        if not Funcionarios.funcionarios:
            limpar_tela()
            Funcionarios.name_app()
            print('\nNenhum funcionário cadastrado.')
            input('\n(Digite Enter para continuar)')
        
        else:
            print('\nSeus funcionários são:')
            for funcionario in Funcionarios.funcionarios:
                nome = funcionario['nome']
                setor = funcionario['setor']
                codigo_funcionario = funcionario['codigo_funcionario']    
                print(f'\n--> Nome: {nome} | Setor: {setor} | Código: {codigo_funcionario}')
            input('\n(Digite Enter para continuar)')
                
    def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
        limpar_tela()
        Funcionarios.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente a seu funcinario')
        print('\n Cadastro concluido com succeso')
        input('\n Pressione Enter para continuar')

    def mostrar_opcoes_funcionarios(): #mostra as opçoes que o usuario pode escolher
        print('\n1 - Todos os funcionarios')
        print('2 - Cadastrar funcionario')
        print('3 - Voltar ao menu principal')

    def checagem_funcionarios():  # Checa a escolha que o usuário fez
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
                    Funcionarios.menu_funcionacios()
                    break

                elif escolha == 2:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.cadastrar_funcionario()
                    Funcionarios.cadastrar_outro_funcionario()
                    Funcionarios.menu_funcionacios()
                    break
                
                else:
                    limpar_tela()
                    Main.main()
                    break

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Funcionarios.name_app()
                Funcionarios.mostrar_opcoes_funcionarios()
                erro_de_valor()
        
    def main_funcionarios(): #executa as funções na ordem certo
        limpar_tela()
        Funcionarios.name_app()
        Funcionarios.mostrar_opcoes_funcionarios()
        Funcionarios.checagem_funcionarios()

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

    def checagem_main(): #Faz a checagem e autenticação da escolha
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
                    Produtos.main_produtos()
                    Main.executar_programa()
                    break
                
                elif escolha == 2:
                    Pedidos.main_pedidos()
                    Main.executar_programa()
                    break
                elif escolha == 3:
                    Estoque.main_estoque()
                    Main.executar_programa()
                    break
                
                elif escolha == 4:
                    Financeiro.executar_programa()
                    Main.executar_programa()
                    break
                
                elif escolha == 5:
                    Funcionarios.main_funcionarios()
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
        Main.checagem_main()
        
Main.executar_programa()# mostra o programa na tela 