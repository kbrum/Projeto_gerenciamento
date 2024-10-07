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
    
funcionarios = [{'nome' : 'joão', 'setor' : 'T.I', 'codigo de funcionario' : 30}]

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
            nv_funcionario = input('\n------------->')
    
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

def cadastrar_funcionario(): #cadastra novo funcionario
    while True:
        try:
            print('\nQual o nome do seu funcionario?')
            nome = input('\n------------->').strip()
            if not nome:
                while True:
                    Funções_basicas.limpar_tela()
                    name_app()
                    print('\nEste campo não pode ficar em branco')
                    print('\nQual o nome do seu funcionario?')
                    nome = input('\n------------->').strip()
                
                    if nome:
                        break   
               
            print('\nQual o setor do seu funcionarios?(ex: RH, Administração, T.I)')
            setor = input('\n------------->').strip()
            if not setor:
                while True:
                    print('\nEste campo não pode ficar em branco')
                    print('\nQual o setor do seu funcionario?')
                    setor = input('\n------------->').strip()
                
                    if setor:
                        break    
            
            codigo_produto = gerador.pro_num()
            
            funcionarios_di = {'nome' : nome,
                               'setor' : setor,
                               'codigo_funcionario' : codigo_produto}
            funcionarios.append(funcionarios_di)
            cadastro_feito()
            break
        
        except:
           Funções_basicas.limpar_tela()
           name_app()
           print('\nEste campo não pode ficar em branco')
           cadastrar_funcionario()
           break

def mostrar_funcionarios():
    ...
  
def mostrar_opcoes_funcionarios(): #mostra as opçoes que o usuario pode escolher
    print('\n1 - Todos os funcionarios')
    print('2 - Cadastrar funcionario')
    print('3 - Voltar ao menu')

def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    print('\n Um codigo de produto foi dado automaticamente a seu produto')
    print('\n Cadastro concluido com succeso')
    input('\n Pressione enter para continuar')

def checagem_funcionarios(): #checa a escolha q o usuario fez
    while True:
        try:
            print('\nEscolha uma opção')
            escolha_funcioanrio = int(input('\n-------------> '))
            
            if escolha_funcioanrio == 1:
                Funções_basicas.limpar_tela()
                name_app()
                
            elif escolha_funcioanrio == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_funcionario()
                Funções_basicas.erro_de_valor()
                cadastrar_outro_funcionario()
                Funções_basicas.erro_de_valor()
                name_app()
                main_funcionarios()
                break
            
        except:
            Funções_basicas.limpar_tela()
            name_app()
            break
        
def main_funcionarios(): #executa as funções na ordem certo
    name_app()
    mostrar_opcoes_funcionarios()
    checagem_funcionarios()
    
def executar_programa(): #executa o programa
    main_funcionarios()

executar_programa() #usado para teste unitarios