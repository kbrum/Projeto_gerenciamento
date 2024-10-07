import Funções_basicas

def name_app():
    print('''
███████╗░██████╗░██╗░░░██╗██╗██████╗░███████╗
██╔════╝██╔═══██╗██║░░░██║██║██╔══██╗██╔════╝
█████╗░░██║██╗██║██║░░░██║██║██████╔╝█████╗░░
██╔══╝░░╚██████╔╝██║░░░██║██║██╔═══╝░██╔══╝░░
███████╗░╚═██╔═╝░╚██████╔╝██║██║░░░░░███████╗
╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝╚═╝░░░░░╚══════╝''')
class codigo_funcionario: #gera um codigo de produto autoincrementavel
    def __init__(self):
        self.codigo = 0
        
    def pro_num(self):
        self.codigo +=1
        return self.codigo
gerador = codigo_funcionario() #instacia do gerador de codigo
    
def menu_funcionacios(): #pergunta ao usuario se quer voltar ao menu 
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
                main_funcionarios()
                break
            
        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            menu_funcionacios()
            break

def cadastrar_outro_funcionario(): #pergunta se quer cadastrar outro funcionario
    while True:
        try:
            Funções_basicas.limpar_tela()
            name_app()
            print('\nDeseja cadastrar outro funcionario')
            print('1 - Sim')
            print('2 - Não')
            nv_funcionario = int(input('\n------------->'))
    
            if nv_funcionario == 1:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_funcionario()
            
            elif nv_funcionario == 2:
                break
            
        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            cadastrar_outro_funcionario()
            break

funcionarios = []

def cadastrar_funcionario():  # Função para cadastrar um novo funcionário
    while True:
        try:
            print('\nQual o nome do seu funcionário?')
            nome = input('\n-------------> ').strip()
            while not nome:
                Funções_basicas.limpar_tela()
                name_app()
                print('\nEste campo não pode ficar em branco')
                print('\nQual o nome do seu funcionário?')
                nome = input('\n-------------> ').strip()

            print('\nQual o setor do seu funcionário? (ex: RH, Administração, T.I)')
            setor = input('\n-------------> ').strip()
            while not setor:
                print('\nEste campo não pode ficar em branco')
                print('\nQual o setor do seu funcionário? (ex: RH, Administração, T.I)')
                setor = input('\n-------------> ').strip()

            codigo_funcionario = gerador.pro_num()

            # Armazena o novo funcionário
            funcionario_di = {
                'nome': nome,
                'setor': setor,
                'codigo_funcionario': codigo_funcionario
            }
            funcionarios.append(funcionario_di)

            cadastro_feito()  # Função para notificar que o cadastro foi feito
            break

        except Exception as e:
            Funções_basicas.limpar_tela()
            name_app()
            print(f'\nErro: {e}')
            print('\nEste campo não pode ficar em branco.')
            cadastrar_funcionario()
            break

def mostrar_funcionarios():  # Função para mostrar os funcionários cadastrados
    if funcionarios:
        print('\nSeus funcionários são:')
        for funcionario in funcionarios:
            nome = funcionario['nome']
            setor = funcionario['setor']
            codigo_funcionario = funcionario['codigo_funcionario']  # Chave corrigida
            print(f'\n--> Nome: {nome} | Setor: {setor} | Código: {codigo_funcionario}')
    else:
        Funções_basicas.limpar_tela()
        name_app()
        print('\nNenhum funcionário cadastrado.')
        input('\nPressione Enter para continuar.')

def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    print('\n Um codigo de funcionario foi dado automaticamente a seu funcinario')
    print('\n Cadastro concluido com succeso')
    input('\n Pressione Enter para continuar')

def mostrar_opcoes_funcionarios(): #mostra as opçoes que o usuario pode escolher
    print('\n1 - Todos os funcionarios')
    print('2 - Cadastrar funcionario')
    print('3 - Voltar ao menu')

def checagem_funcionarios(): #checa a escolha q o usuario fez
    while True:
        try:
            print('\nEscolha uma opção')
            escolha_funcioanrio = int(input('\n-------------> '))
            
            if escolha_funcioanrio == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_funcionarios()
                menu_funcionacios()
                break
                
            elif escolha_funcioanrio == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_funcionario()
                cadastrar_outro_funcionario()
                menu_funcionacios()
                break
            
        except:
            Funções_basicas.limpar_tela()
            name_app()
            mostrar_opcoes_funcionarios()
            Funções_basicas.erro_de_valor()
            checagem_funcionarios()
            break
        
def main_funcionarios(): #executa as funções na ordem certo
    name_app()
    mostrar_opcoes_funcionarios()
    checagem_funcionarios()
    
def executar_programa(): #executa o programa
    main_funcionarios()

executar_programa() #usado para teste unitarios