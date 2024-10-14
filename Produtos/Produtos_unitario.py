from Funcionalidades.Utils import *
from Funcionalidades.Geradorores import *
from Funcionalidades.Solicitações import *
from Funcionalidades.Construtores import Novo_produto

class Produtos:
    def name_app():
        print('''
    ██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
    ██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
    ██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░ ░░██║░░██║░╚═══██╗
    ██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░''')
        
    gerador = Codigo()

    produtos = []

    def cadastrar_produto():  # Função para cadastrar um novo produto
        while True:
            try:
                nome = solicitar_entrada('Qual o nome do seu produto?', 'nome', Produtos).title()
                tipo = solicitar_entrada('Qual o tipo do seu produto? (ex: Calçado, Vestuário, Eletrônico)', 'tipo', Produtos)
                subsecao = solicitar_entrada('Qual a subseção do seu produto? (ex: Tenis, Camisa regata, Camisa social)', 'subseção', Produtos)
                quantidade = solicitar_quantidade(Produtos)
                valor = solicitar_valor('Produtos')
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
                    Produtos.name_app()
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
        
#Produtos.executar_programa() #usado para testes unitarios(Por padrao desabilitado)
    
