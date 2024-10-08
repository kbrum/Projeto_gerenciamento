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
            
            elif menu == 1: # volta ao menu de funcionarios
                Funções_basicas.limpar_tela()
                main_funcionarios()
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            input('\n(Digite Enter para continuar)')

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

def solicitar_entrada(mensagem, setor):  # Função para garantir que a entrada não esteja em branco
    while True:
        entrada = input(f'\n{mensagem}\n------------->').strip()
        if entrada:
            return entrada
        else:
            Funções_basicas.limpar_tela()
            name_app()
            print(f'\nO {setor} do seu funcionario não pode ficar em branco.')

funcionarios = []

def cadastrar_funcionario():  # Função para cadastrar um novo funcionário
    while True:
        try:
            nome = solicitar_entrada('Qual o nome do seu funcionario?', 'nome')
            setor = solicitar_entrada('Qual o setor do seu funcionario?', 'setor')

            codigo_funcionario = gerador.pro_num()

            # Armazena o novo funcionário
            funcionario_di = {
                'nome': nome,
                'setor': setor,
                'codigo_funcionario': codigo_funcionario}
            
            funcionarios.append(funcionario_di)

            cadastro_feito()  # Função para notificar que o cadastro foi feito
            break

        except Exception as e:
            Funções_basicas.limpar_tela()
            name_app()
            print(f'\nErro: {e}')
            print('\nEste campo não pode ficar em branco.')

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
        input('\n(Digite Enter para continuar)')

def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    Funções_basicas.limpar_tela()
    name_app()
    print('\n Um codigo de funcionario foi gerado automaticamente a seu funcinario')
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