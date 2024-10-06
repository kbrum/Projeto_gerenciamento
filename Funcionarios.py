import Funções_basicas
def name_app():
    print('''
███████╗░██████╗░██╗░░░██╗██╗██████╗░███████╗
██╔════╝██╔═══██╗██║░░░██║██║██╔══██╗██╔════╝
█████╗░░██║██╗██║██║░░░██║██║██████╔╝█████╗░░
██╔══╝░░╚██████╔╝██║░░░██║██║██╔═══╝░██╔══╝░░
███████╗░╚═██╔═╝░╚██████╔╝██║██║░░░░░███████╗
╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝╚═╝░░░░░╚══════╝''')
    

def menu_funcionarios(): #pergunta ao usuario se quer voltar ao menu 
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
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                Funções_basicas.erro_de_valor()
                menu_funcionarios()
                break

        except:
            Funções_basicas.limpar_tela()
            name_app()
            Funções_basicas.erro_de_valor()
            menu_funcionarios()
            break

funcionarios = [{'nome' : 'funcionario exemplo', 'setor' : 'setor exemplo', 'codigo de funcionario' : 20}]

def mostrar_funcionarios(): #mostra todos os funcinarios
    print('\nSeu funcionarios são:\n')
    for funcionario in funcionarios:
        setor = funcionario['setor']
        nomes = funcionario['nome']
        codigo_de_funcionario = funcionario['codigo de funcionario']
        print(f'-->  {nomes} | {setor} | {codigo_de_funcionario}')
        
class codigo_produto: #gera um codigo de funcionario autoincrementavel
    def __init__(self):
        self.codigo = 0
        
    def pro_num(self):
        self.codigo +=1
        return self.codigo
    
gerador = codigo_produto()

def cadastro_feito(): #mostra mensagem de cadastro bem sucedido
    print('\n Um codigo de funcionario foi dado automaticamente a seu funcionario')
    print('\n Cadastro concluido com succeso')
    input('\n Pressione enter para continuar')

def cadastrar_outro_funcionario(): #pergunta se quer cadastrar outro funcionario
    while True:
        try:
            Funções_basicas.limpar_tela
            name_app()
            print('\nDeseja cadastrar outro funciorio?')
            print('1 - Sim')
            print('2 - Não')
            Nv_funcionario = input('\n-------------> ')
            
            if Nv_funcionario == 2:
                break
            
            elif Nv_funcionario == 1:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_funcionario()
                break
            
            else:
                Funções_basicas.limpar_tela()
                Funções_basicas.erro_de_valor()
                cadastrar_outro_funcionario()
                break

        except:
            Funções_basicas.limpar_tela()
            Funções_basicas.erro_de_valor()
            cadastrar_outro_funcionario()
            break

def cadastrar_funcionario(): #cadastrar um novo funcionario
    while True:
        try:
            print('\nQual o nome do seu funcionario')
            nome = input('\n------------->')
            
            print('\nQual o tipo do setor(ex: infra, RH, Adm)')
            setor= input('\n------------->')

            codigo = gerador.pro_num()
            
            funcionarios_di = {'nome' : nome,'setor' : setor,'codigo de produto' : codigo}
            
            funcionarios.append(funcionarios_di)
            cadastro_feito()
            break
        except:
            Funções_basicas.limpar_tela()
            Funções_basicas.preço_erro()
            name_app()
            cadastrar_funcionario()
            break

def mostrar_opcoes_funcionarios(): #mostra as opções que o usuario pode escolher
    print('\n1 - Todos os funcionarios')
    print('2 - Cadastrar funcionario')
    print('3 - Voltar ao menu')
    
def checagem_funcionarios(): #faz a checagem doq foi escolhido entre os mostrados acima
    while True:
        try:
            print('\nEscolha uma opção')
            escolha_funcionario = input('\n-------------> ')
            
            if escolha_funcionario == 1:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_funcionarios()
                print('\n')
                menu_funcionarios()
                break
            
            elif escolha_funcionario == 2:
                Funções_basicas.limpar_tela()
                name_app()
                cadastrar_funcionario()
                print('\n')
                Funções_basicas.limpar_tela()
                cadastrar_outro_funcionario()
                cadastrar_outro_funcionario()
                cadastrar_outro_funcionario()
                cadastrar_outro_funcionario()
                Funções_basicas.limpar_tela()
                name_app()
                menu_funcionarios()
                break
            
            elif escolha_funcionario == 3:
                Funções_basicas.limpar_tela()
                print('não implementado ainda')
                break
            
            else:
                Funções_basicas.limpar_tela()
                name_app()
                mostrar_opcoes_funcionarios()
                Funções_basicas.erro_de_valor()
                checagem_funcionarios()
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