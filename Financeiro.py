import Funções_basicas

def name_app(): #titulo
    print('''
███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗██╗██████╗░░█████╗░
██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██║██╔══██╗██╔══██╗
█████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░██║██████╔╝██║░░██║
██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░██║██╔══██╗██║░░██║
██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗██║██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░''')
    
saldo = 1000.00 #variavel que guarda o saldo
class codigo_conta: #gera um codigo de produto autoincrementavel
    def __init__(self):
        self.codigo = 0
        
    def pro_num(self):
        self.codigo +=1
        return self.codigo
gerador = codigo_conta() #instacia do gerador de codigo

def menu_financeiro(): #pergunta ao usuario se quer voltar ao menu financeiro
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
            
            elif menu == 1: # volta ao menu de financeiro
                Funções_basicas.limpar_tela()
                main_financeiro()
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            input('\n(Digite Enter para continuar)')

def menu_contas_a_pagar(): #pergunta ao usuario se quer voltar ao menu contas a pagar
    while True:
        try:
            Funções_basicas.limpar_tela()
            name_app()
            print('\nDeseja voltar ao menu financeiro? ')
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
            
            elif menu == 1: # volta ao menu de financeiro
                Funções_basicas.limpar_tela()
                main_contas_a_pagar()
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            Funções_basicas.limpar_tela()
            name_app()
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

def cadastrar_outra_conta(): #pergunta se quer cadastrar outra conta
    while True:
        try:
            Funções_basicas.limpar_tela()
            name_app()
            print('\nDeseja cadastrar outra conta?')
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
                cadastrar_conta()
            
            elif nv_produto == 2:
                break
            
        except ValueError:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            input('\n(Digite Enter para continuar)')
    
contas_a_pagar = [] #lista do contas a pagar

def solicitar_valor():  # Função para garantir que o preço seja numérico
    while True:
        try:
            print('\nQual o valor da sua conta? (Insira apenas números)')
            preço = float(input('\n------------->').strip())
            if preço > 0:
                return preço
            else:
                Funções_basicas.limpar_tela()
                name_app()
                print('O valor do produto deve ser positivo.')
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
            print(f'\nO {tipo} do seu produto não pode ficar em branco.')

def cadastrar_conta(): #cadastra uma conta
    while True:
        try:
            nome = solicitar_entrada('Qual o nome da sua conta?', 'nome')
            tipo = solicitar_entrada('Qual o tipo da sua conta? (ex: Salário, Água, luz)', 'tipo')
            dados_recebedor = solicitar_entrada('Qual o CPF ou CNPJ do recebed', 'dado do recebedor')
            valor = solicitar_valor()
            
            codigo_conta = gerador.pro_num()  # Substitua por sua função geradora de código

            #armazena uma nova conta
            contas_di = {
                'nome': nome,
                'tipo': tipo,
                'dados do recebedor' : dados_recebedor,
                'valor': valor,
                'codigo de conta': codigo_conta}
            
            contas_a_pagar.append(contas_di)
            
            cadastro_feito()  # Confirma o cadastro da conta
            break 

        except ValueError:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.preço_erro()
    
def mostrar_contas_a_pagar(): # mostra as contas2
    if not contas_a_pagar:
        Funções_basicas.limpar_tela()
        name_app()
        print('\nNenhuma conta cadastrada.')
        input('\nPressione Enter para continuar.')
    else:
        print('\nSuas contas:')
        for conta in contas_a_pagar:
            nome = conta['nome']
            tipo = conta['tipo']
            dados_recebedor = conta['dados do recebedor']
            valor = conta['valor']
            codigo_de_conta = conta['codigo de conta']
            
            try:
                if len(dados_recebedor) == 11:
                    dados_recebedor = formatar_cpf(dados_recebedor)
                elif len(dados_recebedor) == 14:
                    dados_recebedor = formatar_cnpj(dados_recebedor)
                else:
                    raise ValueError("CPF/CNPJ inválido.")
            except ValueError as e:
                print(f"\nErro: {e}. Não foi possível formatar o CPF/CNPJ.")
            
            print(f'\n--> Nome: {nome} | Tipo: {tipo} | CPF/CNPJ do recebedor: {dados_recebedor} | Valor R${valor:.2f} | Código: {codigo_de_conta}')
            
        input('\n(Digite Enter para continuar)')

def mostrar_saldo(): #mostra o saldo
    print(f'\nSeu saldo é de R$: {saldo}')
    input('\n(Digite Enter para continuar)')

def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    Funções_basicas.limpar_tela()
    name_app()
    print('\n Um codigo de identificação foi gerado automaticamente a sua despesa')
    print('\n Cadastro concluido com succeso')
    input('\n Pressione enter para continuar')

def mostrar_opcoes_contas_a_pagar(): #mostra as opções que o usuario pode escolher no contas a pagar
    print('\n1 - Ver todas as contas a pagar')
    print('2 - Cadastrar contas')
    print('3 - Voltar ao menu financeiro')

def checagem_contas_a_pagar(): #faz a checagem doq foi no contas a pagar
    while True:
        try:
            print('\nEscolha uma opção')
            
            # Captura a entrada e remove espaços em branco
            escolha = input('\n-------------> ').strip()
    
            # Verifica se a entrada está vazia
            if not escolha:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_contas_a_pagar()
                print('\nA escolha não pode ficar em branco.')
                continue 

            # Tenta converter para número inteiro
            escolha = int(escolha)

            # Verifica as opções
            if escolha == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_contas_a_pagar()
                menu_contas_a_pagar()
                break

            elif escolha == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_conta()
                cadastrar_outra_conta()
                menu_contas_a_pagar()
                break
            
            elif escolha == 3:
                main_financeiro()
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_financeiro()
                print('Por favor, escolha uma opção válida.')

        except ValueError:  # Captura erros de conversão de string para int
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_financeiro()
            Funções_basicas.erro_de_valor()

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
                name_app()
                mostrar_opcoes_financeiro()
                print('\nA escolha não pode ficar em branco.')
                continue 

            # Tenta converter para número inteiro
            escolha = int(escolha)

            # Verifica as opções
            if escolha == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_saldo()
                menu_financeiro()
                break

            elif escolha == 2:
                Funções_basicas.limpar_tela()
                name_app()
                main_contas_a_pagar()
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_financeiro()
                print('Por favor, escolha uma opção válida.')

        except ValueError:  # Captura erros de conversão de string para int
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_financeiro()
            Funções_basicas.erro_de_valor()

def main_contas_a_pagar(): # agrupa e executa as funçoes do conta a pagar
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opcoes_contas_a_pagar()
    checagem_contas_a_pagar()
    
def main_financeiro(): #executa todas as funções na ordem certa
    Funções_basicas.limpar_tela()
    name_app()
    mostrar_opcoes_financeiro()
    checagem_financeiro()
    
def executar_programa(): #mostra o programa na tela
    main_financeiro()

executar_programa() #usado para testes unitarios