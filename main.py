import os

class Funções_basicas: #Funções que sao muito usadas
    
    def variavel_em_branco(): #caso o usuario na digite nada
        print('\nEste campo não pode ficar em branco')

    def preço_erro(): #erro de preço de produto
        print('\n Insira um Preço valido(APENAS NUMEROS)')

    def erro_de_valor(): # aparece quando se digita algo que não é numero
        print('\nPor favor, selecione uma opção valida\n')

    def limpar_tela(): #Meio óbvio...
        os.system('cls')

class codigo: #Gera um codigo de produto/funcionario/conta autoincrementavel
    def __init__(self):
        self.codigo = 0
            
    def pro_num(self):
        self.codigo +=1
        return self.codigo
    
class Produtos: #Produtos
    def name_app():
        print('''
    ██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗████████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝
    ██████╔╝██████╔╝██║░░██║██║░░██║██║░░░██║░░░██║░░░██║░░██║╚█████╗░
    ██╔═══╝░██╔══██╗██║░░██║██║░░██║██║░░░██║░░░██║░ ░░██║░░██║░╚═══██╗
    ██║░░░░░██║░░██║╚█████╔╝██████╔╝╚██████╔╝░░░██║░░░╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░╚═════╝░''')
        

    gerador = codigo() #instacia do gerador de codigo

    def menu_produtos(): #pergunta ao usuario se quer voltar ao menu produtos
        while True:
                try:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    print('\nDeseja voltar ao menu? ')
                    print('1 - Sim')
                    print('2 - Não')
                    
                    menu = input('\n-------------> ').strip()
                    
                    if not menu: # verifica se a entrada do menu não é vazia
                        Funções_basicas.limpar_tela()
                        Produtos.name_app()
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
                        Produtos.main_produtos()
                        break
                    
                except ValueError: #em caso de inserir algo que não é numero na opção
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    Funções_basicas.erro_de_valor()
                    input('\n(Digite Enter para continuar)')

    def cadastrar_outro_produto(): #pergunta se quer cadastrar outro produto
        while True:
            try:
                Funções_basicas.limpar_tela()
                Produtos.name_app()
                print('\nDeseja cadastrar outro produto?')
                print('1 - Sim')
                print('2 - Não')
                
                nv_produto = input('\n-------------> ').strip()
                
                if not nv_produto:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                    
                nv_produto = int(nv_produto)
        
                if nv_produto == 1:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    Produtos.cadastrar_produto()
                
                elif nv_produto == 2:
                    break
                
            except ValueError:
                Funções_basicas.limpar_tela()
                Produtos.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def solicitar_preco():  # Função para garantir que o preço seja numérico e positivo
        while True:
            try:
                print('\nQual o preço do seu produto? (Insira apenas números)')
                preço = float(input('\n------------->').strip())
                if preço > 0:
                    return preço
                else:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    print('O preço do produto deve ser positivo.')
            except ValueError:
                Funções_basicas.limpar_tela()
                Produtos.name_app()
                Funções_basicas.preço_erro()

    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                Funções_basicas.limpar_tela()
                Produtos.name_app()
                print(f'\nA parte de {tipo} do seu produto não pode ficar em branco.')

    produtos = []
    
    def cadastrar_produto():  # Função para cadastrar um novo produto
        while True:
            try:
                nome = Produtos.solicitar_entrada('Qual o nome do seu produto?', 'nome')
                tipo = Produtos.solicitar_entrada('Qual o tipo do seu produto? (ex: Calçado, Vestuário, Eletrônico)', 'tipo')
                subsecao = Produtos.solicitar_entrada('Qual a subseção do seu produto? (ex: Tenis, Camisa regata, Camisa social)', 'subseção')
                preço = Produtos.solicitar_preco()
                
                codigo_produto = Produtos.gerador.pro_num()  # Substitua por sua função geradora de código

                #armazena um novo produto
                produto_di = {
                    'nome': nome,
                    'preço': preço,
                    'tipo': tipo,
                    'subseção' : subsecao,
                    'codigo de produto': codigo_produto}
                
                Produtos.produtos.append(produto_di)
                
                Produtos.cadastro_feito()  # Confirma o cadastro do produto
                break 

            except ValueError:
                Funções_basicas.limpar_tela()
                Produtos.name_app()
                Funções_basicas.preço_erro()
                
    def mostrar_produtos():  # Função para mostrar todos os produtos cadastrados
        if not Produtos.produtos:
            Funções_basicas.limpar_tela()
            Produtos.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
        else:
            print('\nSeus produtos são:')
            for produto in Produtos.produtos:
                nome = produto['nome']
                tipo = produto['tipo']
                subsecao = produto['subseção']
                preço = produto['preço']
                codigo_de_produto = produto['codigo de produto']
                print(f'\n--> Nome: {nome} | Seção: {tipo} | Subseção: {subsecao} | Preço: R${preço:.2f} | Código: {codigo_de_produto} |')
            input('\n(Digite Enter para continuar)')
            
    def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
        Funções_basicas.limpar_tela()
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
                escolha_funcionario = input('\n-------------> ').strip()
        
                # Verifica se a entrada está vazia
                if not escolha_funcionario:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    Produtos.mostrar_opcoes_produtos()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha_funcionario = int(escolha_funcionario)

                # Verifica as opções
                if escolha_funcionario == 1:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    Produtos.mostrar_produtos()
                    Produtos.menu_produtos()
                    break

                elif escolha_funcionario == 2:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    Produtos.cadastrar_produto()
                    Produtos.cadastrar_outro_produto()
                    Produtos.menu_produtos()
                    break
                
                elif escolha_funcionario == 3:
                    Funções_basicas.limpar_tela()
                    Main.main()
                
                else:
                    Funções_basicas.limpar_tela()
                    Produtos.name_app()
                    Produtos.mostrar_opcoes_produtos()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                Funções_basicas.limpar_tela()
                Produtos.name_app()
                Produtos.mostrar_opcoes_produtos()
                Funções_basicas.erro_de_valor()
        
    def main_produtos(): #executa todas as funções na ordem certa
        Funções_basicas.limpar_tela()
        Produtos.name_app()
        Produtos.mostrar_opcoes_produtos()
        Produtos.checagem_produtos()

class Estoque: #Estoque
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

    def menu_estoque(): #pergunta ao usuario se quer voltar ao menu 
        while True:
            try:
                Funções_basicas.limpar_tela()
                Estoque.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    Funções_basicas.limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de estoque
                    Funções_basicas.limpar_tela()
                    Estoque.main_estoque()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Estoque.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def Produtos_em_falta():#mostra os produtos em falta
        if Estoque.em_falta:
            print('\nOs produtos em falta são:')
            for produtos_em_falta in Estoque.em_falta:
                print(f'.{produtos_em_falta}')
        else:
            Funções_basicas.limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
                
    def todos_em_estoque(): #mostra todo o estoque
        if Estoque.produtos_em_estoque:
            print('\nProdutos em estoque:')
            for produtos in Estoque.produtos_em_estoque:
                print(f'.{produtos}')
        else:
            Funções_basicas.limpar_tela()
            Estoque.name_app()
            print('\nNenhum produto cadastrado.')
            input('\nPressione Enter para continuar.')
            
    def mostrar_opcoes_estoque(): #mostra a opções q o usuario pode escolher
        print('\n1 - Ver todos')
        print('2 - Produtos em falta')
        print('3 - Voltar ao menu inicial')

    def checagem_estoque(): #faz a checagem doq foi escolhido entre os mostrados acima
        while True:
            try:
                print('\nEscolha uma opção')
                escolha_financeiro = int(input('\n-------------> '))
                
                if escolha_financeiro == 1:
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    Estoque.todos_em_estoque()
                    print('\n')
                    Estoque.menu_estoque()
                    break
                
                elif escolha_financeiro == 2:
                    Funções_basicas.limpar_tela()
                    Estoque.name_app()
                    Estoque.Produtos_em_falta()
                    print('\n')
                    Estoque.menu_estoque()
                    break
                
                elif escolha_financeiro == 3:
                    Funções_basicas.limpar_tela()
                    Main.main()
            
            except:
                Funções_basicas.limpar_tela()
                Estoque.name_app()
                Estoque.mostrar_opcoes_estoque()
                Funções_basicas.erro_de_valor()
                Estoque.checagem_estoque()
                break
        
    def main_estoque(): #executa todas as funções na ordem certa
        Funções_basicas.limpar_tela()
        Estoque.name_app()
        Estoque.mostrar_opcoes_estoque()
        Estoque.checagem_estoque()

class Financeiro:
    def name_app(): #titulo
        print('''
    ███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
    ██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
    █████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
    ██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
    ██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
    ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
        

    gerador = codigo() #instacia do gerador de codigo

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

    def formatar_cpf(cpf): #formata um cpf
        cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere que não seja dígito
        if len(cpf) != 11:
            raise ValueError("O CPF deve ter 11 dígitos.")
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    def formatar_cnpj(cnpj): #formata um cnpj
        cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove qualquer caractere que não seja dígito
        if len(cnpj) != 14:
            raise ValueError("O CNPJ deve ter 14 dígitos.")
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
    
    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                Funções_basicas.limpar_tela()
                Financeiro.name_app()
                print(f'\nO {tipo} do seu produto não pode ficar em branco.')
    
    def solicitar_valor():  # Função para garantir que o preço seja numérico
        while True:
            try:
                print('\nQual o valor da sua conta? (Insira apenas números)')
                preço = float(input('\n------------->').strip())
                if preço > 0:
                    return preço
                else:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    print('O valor do produto deve ser positivo.')
            except ValueError:
                Funções_basicas.limpar_tela()
                Financeiro.name_app()
                Funções_basicas.preço_erro()
        
    def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
        Funções_basicas.limpar_tela()
        Financeiro.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente a sua despesa')
        print('\n Cadastro concluido com succeso')
        input('\n Pressione enter para continuar')
    
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
                        #Main.main()
                    
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
            print(f'\n Seu saldo é de R$: {Financeiro.Saldo.saldo} ')
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
                    print('Digite o CPF ou CNPJ do recebedor')
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
            if not Financeiro.Contas_a_pagar.contas_a_pagar:
                Funções_basicas.limpar_tela()
                Financeiro.name_app()
                print('\nNenhuma conta cadastrada.')
                input('\nPressione Enter para continuar.')
            else:
                print('\nSuas contas:')
                for conta in Financeiro.Contas_a_pagar.contas_a_pagar:
                    nome = conta['nome']
                    tipo = conta['tipo']
                    dados_recebedor = conta['dados do recebedor']
                    valor = conta['valor']
                    codigo_de_conta = conta['codigo de conta']
                    
                    print(f'\n--> Nome: {nome} | Tipo: {tipo} | CPF/CNPJ do recebedor: {dados_recebedor} | Valor R${valor:.2f} | Código: {codigo_de_conta}')
                    
                input('\n(Digite Enter para continuar)')
        
        def cadastrar_conta(): #cadastra uma conta a pagar
            while True:
                try:
                    nome = Financeiro.solicitar_entrada('Qual o nome da sua conta?', 'nome')
                    tipo = Financeiro.solicitar_entrada('Qual o tipo da sua conta? (ex: Salário, Água, luz)', 'tipo')
                    dados_recebedor = Financeiro.Contas_a_pagar.solicitar_dados()
                    valor = Financeiro.solicitar_valor()
                    
                    codigo_conta = Financeiro.gerador.pro_num() 

                    #armazena uma nova conta
                    contas_di = {
                        'nome': nome,
                        'tipo': tipo,
                        'dados do recebedor' : dados_recebedor,
                        'valor': valor,
                        'codigo de conta': codigo_conta}
                    
                    Financeiro.Contas_a_pagar.contas_a_pagar.append(contas_di)
                    
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
                        Financeiro.Contas_a_pagarmenu()
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
                    print('Digite o CPF ou CNPJ do pagante')
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
                    contas_di = {
                        'nome': nome,
                        'tipo': tipo,
                        'dados do paganter' : dados_pagante,
                        'valor': valor,
                        'codigo de conta': codigo_conta}
                    
                    Financeiro.Contas_a_receber.contas_a_receber.append(contas_di)
                    
                    Financeiro.cadastro_feito()  # Confirma o cadastro da conta
                    break 

                except ValueError:
                    Funções_basicas.limpar_tela()
                    Financeiro.name_app()
                    Funções_basicas.preço_erro()     

        def mostrar_contas(): # mostra as contas a pagar
            if not Financeiro.contas_a_receber:
                Funções_basicas.limpar_tela()
                Financeiro.name_app()
                print('\nNenhuma conta cadastrada.')
                input('\nPressione Enter para continuar.')
            else:
                print('\nSuas contas:')
                for conta in Financeiro.Contas_a_receber.contas_a_receber:
                    nome = conta['nome']
                    tipo = conta['tipo']
                    dados_pagante = conta['dados do pagante']
                    valor = conta['valor']
                    codigo_de_conta = conta['codigo de conta']
                    
                    try:
                        if len(dados_pagante) == 11:
                            dados_pagante = Financeiro.formatar_cpf(dados_pagante)
                        elif len(dados_pagante) == 14:
                            dados_pagante = Financeiro.formatar_cnpj(dados_pagante)
                        else:
                            raise ValueError("CPF/CNPJ inválido.")
                    except ValueError as e:
                        print(f"\nErro: {e}. Não foi possível formatar o CPF/CNPJ.")
                    
                    print(f'\n--> Nome: {nome} | Tipo: {tipo} | CPF/CNPJ do pagante: {dados_pagante} | Valor R${valor:.2f} | Código: {codigo_de_conta}')
                    
                input('\n(Digite Enter para continuar)')
                
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

class Funcionarios: #Funcionarios
    def name_app():
        print('''
    ███████╗░██████╗░██╗░░░██╗██╗██████╗░███████╗
    ██╔════╝██╔═══██╗██║░░░██║██║██╔══██╗██╔════╝
    █████╗░░██║██╗██║██║░░░██║██║██████╔╝█████╗░░
    ██╔══╝░░╚██████╔╝██║░░░██║██║██╔═══╝░██╔══╝░░
    ███████╗░╚═██╔═╝░╚██████╔╝██║██║░░░░░███████╗
    ╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝╚═╝░░░░░╚══════╝''')

    gerador = codigo() #instacia do gerador de codigo
        
    def menu_funcionacios(): #pergunta ao usuario se quer voltar ao menu 
        while True:
            try:
                Funções_basicas.limpar_tela()
                Funcionarios.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Funcionarios.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    Funções_basicas.limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de funcionarios
                    Funções_basicas.limpar_tela()
                    Funcionarios.main_funcionarios()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Funcionarios.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')

    def cadastrar_outro_funcionario(): #pergunta se quer cadastrar outro funcionario
        while True:
            try:
                Funções_basicas.limpar_tela()
                Funcionarios.name_app()
                print('\nDeseja cadastrar outro funcionario')
                print('1 - Sim')
                print('2 - Não')
                nv_funcionario = int(input('\n------------->'))
        
                if nv_funcionario == 1:
                    Funções_basicas.limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.cadastrar_funcionario()
                
                elif nv_funcionario == 2:
                    break
                
            except:
                Funções_basicas.limpar_tela()
                Funcionarios.name_app()
                Funções_basicas.erro_de_valor()
                Funcionarios.cadastrar_outro_funcionario()
                break

    def solicitar_entrada(mensagem, setor):  # Função para garantir que a entrada não esteja em branco
        while True:
            entrada = input(f'\n{mensagem}\n------------->').strip()
            if entrada:
                return entrada
            else:
                Funções_basicas.limpar_tela()
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
                Funções_basicas.limpar_tela()
                Funcionarios.name_app()
                print(f'\nErro: {e}')
                print('\nEste campo não pode ficar em branco.')

    def mostrar_funcionarios():  # Função para mostrar os funcionários cadastrados
        if not Funcionarios.funcionarios:
            Funções_basicas.limpar_tela()
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
        Funções_basicas.limpar_tela()
        Funcionarios.name_app()
        print('\n Um codigo de identificação foi gerado automaticamente a seu funcinario')
        print('\n Cadastro concluido com succeso')
        input('\n Pressione Enter para continuar')

    def mostrar_opcoes_funcionarios(): #mostra as opçoes que o usuario pode escolher
        print('\n1 - Todos os funcionarios')
        print('2 - Cadastrar funcionario')
        print('3 - Voltar ao menu')

    def checagem_funcionarios():  # Checa a escolha que o usuário fez
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha_funcionario = input('\n-------------> ').strip()

                # Verifica se a entrada está vazia
                if not escolha_funcionario:
                    Funções_basicas.limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.mostrar_opcoes_funcionarios()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha_funcionario = int(escolha_funcionario)

                # Verifica as opções
                if escolha_funcionario == 1:
                    Funções_basicas.limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.mostrar_funcionarios()
                    Funcionarios.menu_funcionacios()
                    break

                elif escolha_funcionario == 2:
                    Funções_basicas.limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.cadastrar_funcionario()
                    Funcionarios.cadastrar_outro_funcionario()
                    Funcionarios.menu_funcionacios()
                    break
                
                else:
                    Funções_basicas.limpar_tela()
                    Main.main()

            except ValueError:  # Captura erros de conversão de string para int
                Funções_basicas.limpar_tela()
                Funcionarios.name_app()
                Funcionarios.mostrar_opcoes_funcionarios()
                Funções_basicas.erro_de_valor()
        
    def main_funcionarios(): #executa as funções na ordem certo
        Funções_basicas.limpar_tela()
        Funcionarios.name_app()
        Funcionarios.mostrar_opcoes_funcionarios()
        Funcionarios.checagem_funcionarios()
        
    def executar_programa(): #executa o programa
        Funcionarios.main_funcionarios()

class Main: #MAIN
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
        print('2 - Estoque')
        print('3 - Financeiro')
        print('4 - Funcionarios')
        print('5 - Sair')

    def checagem_main(): #Faz a checagem e autenticação da escolha
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha_funcionario = input('\n-------------> ').strip()
        
                # Verifica se a entrada está vazia
                if not escolha_funcionario:
                    Funções_basicas.limpar_tela()
                    Main.name_app()
                    Main.mostrar_opcoes()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha_funcionario = int(escolha_funcionario)

                # Verifica as opções
                if escolha_funcionario == 1:
                    Funções_basicas.limpar_tela()
                    Produtos.main_produtos()
                    break
                
                elif escolha_funcionario == 2:
                    Funções_basicas.limpar_tela()
                    Estoque.main_estoque()
                    break
                
                elif escolha_funcionario == 3:
                    Funções_basicas.limpar_tela()
                    Financeiro.Principal.main_financeiro()
                    break
                
                elif escolha_funcionario == 4:
                    Funções_basicas.limpar_tela()
                    Funcionarios.main_funcionarios()
                    break
                
                elif escolha_funcionario == 5:
                    Funções_basicas.limpar_tela()
                    Main.name_app()
                    confirmacao = input('\nTem certeza que deseja sair? (s/n): ').strip()
                    if confirmacao == 's' or 'S':
                        Funções_basicas.limpar_tela()
                        print('\nFINALIZADO')
                        break
                    else:
                        Funções_basicas.limpar_tela()
                        Main.name_app()
                        Main.mostrar_opcoes()
                
                else:
                    Funções_basicas.limpar_tela()
                    Main.name_app()
                    Main.mostrar_opcoes()
                    print('Por favor, escolha uma opção válida.')

            except ValueError:  # Captura erros de conversão de string para int
                Funções_basicas.limpar_tela()
                Main.name_app()
                Main.mostrar_opcoes()
                Funções_basicas.erro_de_valor()
        
    def main():
        Funções_basicas.limpar_tela()
        Main.name_app()
        Main.mostrar_opcoes()
        Main.checagem_main()
        
    def executar_programa():#executa o programa 
        Main.main()
        
Main.executar_programa()# mostra o programa na tela 