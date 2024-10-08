import Funções_basicas

def name_app():
    print('''
██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░ ░░██║░░██║░╚═══██╗
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
            Funções_basicas.limpar_tela()
            name_app()
            print('\nDeseja voltar ao menu? ')
            print('1 - Sim')
            print('2 - Não')
            
            menu = input('\n-------------> ').strip()
            
            if not menu: # verifica se a entrada do menu não é vazia
                Funções_basicas.limpar_tela()
                name_app()
                print('\nEste campo não pode ficar em branco')
                input('\n(Digite Enter para continuar)')
                continue
            
            menu = int(menu)
            
            if menu == 2: # fecha o programa
                Funções_basicas.limpar_tela()
                print('Finalizado')
                break
            
            elif menu == 1: # volta ao menu de produtos
                Funções_basicas.limpar_tela()
                main_produtos()
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            input('\n(Digite Enter para continuar)')

def cadastrar_outro_produto(): #pergunta se quer cadastrar outro produto
    while True:
        try:
            Funções_basicas.limpar_tela()
            name_app()
            print('\nDeseja cadastrar outro produto?')
            print('1 - Sim')
            print('2 - Não')
            
            nv_produto = input('\n-------------> ').strip()
            
            if not nv_produto:
                Funções_basicas.limpar_tela()
                name_app()
                print('\nEste campo não pode ficar em branco')
                input('\n(Digite Enter para continuar)')
                continue
                
            nv_produto = int(nv_produto)
    
            if nv_produto == 1:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_produto()
            
            elif nv_produto == 2:
                break
            
        except ValueError:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
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
                Funções_basicas.limpar_tela()
                name_app()
                print('O preço do produto deve ser positivo.')
        except ValueError:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.preço_erro()

def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
    while True:
        valor = input(f'\n{mensagem}\n------------->').strip()
        if valor:
            return valor
        else:
            Funções_basicas.limpar_tela()
            name_app()
            print(f'\nA parte de {tipo} do seu produto não pode ficar em branco.')

def cadastrar_produto():  # Função para cadastrar um novo produto
    while True:
        try:
            nome = solicitar_entrada('Qual o nome do seu produto?', 'nome')
            tipo = solicitar_entrada('Qual o tipo do seu produto? (ex: Calçado, Vestuário, Eletrônico)', 'tipo')
            subsecao = solicitar_entrada('Qual a subseção do seu produto? (ex: Tenis, Camisa regata, Camisa social)', 'subseção')
            preço = solicitar_preco()
            
            codigo_produto = gerador.pro_num()  # Substitua por sua função geradora de código

            #armazena um novo produto
            produto_di = {
                'nome': nome,
                'preço': preço,
                'tipo': tipo,
                'subseção' : subsecao,
                'codigo de produto': codigo_produto}
            
            produtos.append(produto_di)
            
            cadastro_feito()  # Confirma o cadastro do produto
            break 

        except ValueError:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.preço_erro()
            
def mostrar_produtos():  # Função para mostrar todos os produtos cadastrados
    if not produtos:
        Funções_basicas.limpar_tela()
        name_app()
        print('\nNenhum produto cadastrado.')
        input('\nPressione Enter para continuar.')
    else:
        print('\nSeus produtos são:')
        for produto in produtos:
            nome = produto['nome']
            tipo = produto['tipo']
            subsecao = produto['subseção']
            preço = produto['preço']
            codigo_de_produto = produto['codigo de produto']
            print(f'\n--> Nome: {nome} | Seção: {tipo} | Subseção: {subsecao} | Preço R${preço:.2f} | Código: {codigo_de_produto} |')
        input('\n(Digite Enter para continuar)')
        
def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    Funções_basicas.limpar_tela()
    name_app()
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
            escolha_funcionario = input('\n-------------> ').strip()
    
            # Verifica se a entrada está vazia
            if not escolha_funcionario:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_produtos()
                print('\nA escolha não pode ficar em branco.')
                continue 

            # Tenta converter para número inteiro
            escolha_funcionario = int(escolha_funcionario)

            # Verifica as opções
            if escolha_funcionario == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_produtos()
                menu_produtos()
                break

            elif escolha_funcionario == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_produto()
                cadastrar_outro_produto()
                menu_produtos()
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_produtos()
                print('Por favor, escolha uma opção válida.')

        except ValueError:  # Captura erros de conversão de string para int
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_produtos()
            Funções_basicas.erro_de_valor()
    
def main_produtos(): #executa todas as funções na ordem certa
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opcoes_produtos()
    checagem_produtos()

def executar_programa():#mostra o programa na tela
    main_produtos()
    
#executar_programa() #usado para testes unitarios(Por padrao desabilitado)