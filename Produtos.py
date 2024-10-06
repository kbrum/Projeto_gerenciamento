import Funções_basicas

def name_app():
    print('''
██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░''')
    
def menu_produtos(): #pergunta ao usuario se quer voltar ao menu 
    while True:
        try:
            print('\nDeseja voltar ao menu? ')
            print('1 - Sim')
            print('2 - Não')
            menu = int(input('\n-------------> '))
            
            if menu == 2:
                Funções_basicas.limpar_tela()
                print('Finalizado')
                break
            
            elif menu == 1:
                Funções_basicas.limpar_tela()
                main_produtos()
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                Funções_basicas.erro_de_valor()
                menu_produtos()
                break

        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            menu_produtos()
            break

produtos = [{'nome' : 'produto exemplo', 'tipo' : 'tipo exemplo', 'preço' : 23.50, 'codigo de produto' :20}]

def mostrar_produtos(): #mostra todos os produtos
    print('\nSeu produtos são:\n')
    for produto in produtos:
        preços = produto['preço']
        nomes = produto['nome']
        tipos = produto['tipo']
        codigo_de_produto = produto['codigo de produto']
        print(f'-->  {nomes} | {tipos} | R$: {preços} | {codigo_de_produto}') 

def cadastrar_outro_produto(): #pergunta se quer cadastrar outro produto
    while True:
        try:
            Funções_basicas.limpar_tela
            name_app()
            print('\nDeseja cadastrar outro produto?')
            print('1 - Sim')
            print('2 - Não')
            Nv_produto = int(input('\n-------------> '))
            
            if Nv_produto == 2:
                break
            
            elif Nv_produto == 1:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_produto()
                break
            
            else:
                Funções_basicas.limpar_tela()
                Funções_basicas.erro_de_valor()
                cadastrar_outro_produto()
                break

        except:
            Funções_basicas.limpar_tela()
            Funções_basicas.erro_de_valor()
            cadastrar_outro_produto()
            break
    
def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    print('\n Um codigo de produto foi dado automaticamente a seu produto')
    print('\n Cadastro concluido com succeso')
    input('\n Pressione enter para continuar')
   
class codigo_produto: #gera um codigo de produto autoincrementavel
    def __init__(self):
        self.codigo = 0
        
    def pro_num(self):
        self.codigo +=1
        return self.codigo

gerador = codigo_produto()

def cadastrar_produto(): #cadastrar um novo produto
    while True:
        try:
            print('\nQual o nome do seu produto')
            nome = input('\n------------->')
            
            print('\nQual o tipo do seu produto(ex: Calçado, Vestuario, Eletrônico)')
            tipo = input('\n------------->')
            
            print('\nQual o valor do seu produto(Insira apenas numeros)')
            preço = float(input('\n------------->')) 
            
            codigo = gerador.pro_num()
            
            produto_di = {'nome' : nome,
                          'preço' : preço, 
                          'tipo' : tipo, 
                          'codigo de produto' : codigo}
            
            produtos.append(produto_di)
            cadastro_feito()
            break
        except:
            Funções_basicas.limpar_tela()
            Funções_basicas.preço_erro()
            name_app()
            cadastrar_produto()
            break
            
def mostrar_opcoes_produtos(): #mostra as opções que o usuario pode escolher
    print('\n1 - Todos os produtos')
    print('2 - Cadastrar produto')
    print('3 - Voltar ao menu')
       
def checagem_produtos(): #faz a checagem doq foi escolhido entre os mostrados acima
    while True:
        try:
            print('\nEscolha uma opção')
            escolha_financeiro = int(input('\n-------------> '))
            
            if escolha_financeiro == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_produtos()
                print('\n')
                menu_produtos()
                break
            
            elif escolha_financeiro == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_produto()
                print('\n')
                Funções_basicas.limpar_tela()
                cadastrar_outro_produto()
                cadastrar_outro_produto()
                cadastrar_outro_produto()
                cadastrar_outro_produto()
                Funções_basicas.limpar_tela()
                name_app()
                menu_produtos()
                break
            
            elif escolha_financeiro == 3:
                Funções_basicas.limpar_tela()
                print('não implementado ainda')
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_produtos()
                Funções_basicas.erro_de_valor()
                checagem_produtos()
                break
            
        except:
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_produtos()
            Funções_basicas.erro_de_valor()
            checagem_produtos()
            break
    
def main_produtos(): #executa todas as funções na ordem certa
    name_app()
    mostrar_opcoes_produtos()
    checagem_produtos()

def executar_programa(): #mostra o programa na tela
    main_produtos()
    
executar_programa() #usado para testes unitarios