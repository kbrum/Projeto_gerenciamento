import Funções_basicas

def name_app():
    print('''
██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░''')
    
class codigo_produto: #gera um codigo de produto autoincrementavel
    def __init__(self):
        self.codigo = 0
        
    def pro_num(self):
        self.codigo +=1
        return self.codigo
gerador = codigo_produto() #instacia do gerador de codigo

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
            
        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            menu_produtos()
            break

def cadastrar_outro_produto(): #pergunta se quer cadastrar outro produto
    while True:
        try:
            Funções_basicas.limpar_tela()
            name_app()
            print('\nDeseja cadastrar outro produto?')
            print('1 - Sim')
            print('2 - Não')
            Nv_produto = int(input('\n-------------> '))
            
            if Nv_produto == 1:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_produto()
            
            elif Nv_produto == 2:
                break
        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            cadastrar_outro_produto()
            break

produtos = []

def cadastrar_produto():  # Função para cadastrar um novo produto
    while True:
        try:
            Funções_basicas.limpar_tela()
            name_app()
            print('\nQual o nome do seu produto?')
            nome = input('\n------------->').strip()
            if not nome:  # Verifica se o nome foi preenchido
                print("\nO nome do produto não pode ficar em branco.")
                continue

            print('\nQual o tipo do seu produto? (ex: Calçado, Vestuário, Eletrônico)')
            tipo = input('\n------------->').strip()
            if not tipo:  # Verifica se o tipo foi preenchido
                print("\nO tipo do produto não pode ficar em branco.")
                continue

            print('\nQual o valor do seu produto? (Insira apenas números)')
            preço = input('\n------------->').strip()
            if not preço.replace('.', '', 1).isdigit():  # Verifica se o preço é válido (números e ponto)
                print("\nPor favor, insira um valor válido para o preço (apenas números).")
                continue

            preço = float(preço)  # Converte o preço para float

            codigo = gerador.pro_num()  # Substitua por sua função geradora de código

            produto_di = {
                'nome': nome,
                'preço': preço,
                'tipo': tipo,
                'codigo de produto': codigo
            }

            produtos.append(produto_di)
            cadastro_feito()  # Confirma o cadastro do produto
            break  # Sai do loop após o cadastro bem-sucedido

        except Exception as e:
            Funções_basicas.limpar_tela()
            Funções_basicas.preço_erro()  # Função para exibir erro de preço
            name_app()
            print(f"\nErro: {e}")  # Exibe a mensagem de erro
            continue  # Continua o loop para tentar novamente

def mostrar_produtos():  # Função para mostrar todos os produtos cadastrados
    if produtos:
        print('\nSeus produtos são:\n')
        for produto in produtos:
            nome = produto['nome']
            tipo = produto['tipo']
            preço = produto['preço']
            codigo_de_produto = produto['codigo de produto']
            print(f'--> {nome} | {tipo} | R$: {preço:.2f} | Código: {codigo_de_produto}')
    else:
        Funções_basicas.limpar_tela()
        name_app()
        print('\nNenhum produto cadastrado.')
        input('\nPressione Enter para continuar.')

def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    print('\n Um codigo de produto foi dado automaticamente a seu produto')
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
            escolha_financeiro = int(input('\n-------------> '))
            
            if escolha_financeiro == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_produtos()
                menu_produtos()
                break
            
            elif escolha_financeiro == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_produto()
                cadastrar_outro_produto()
                menu_produtos()
                break
            
            elif escolha_financeiro == 3:
                Funções_basicas.limpar_tela()
                print('não implementado ainda')
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
    
#executar_programa() #usado para testes unitarios