import Funções_basicas
class Funcionarios:
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
                    Funcionarios.name_app()
                    Funcionarios.mostrar_opcoes_funcionarios()
                    print('Por favor, escolha uma opção válida.')

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

Funcionarios.executar_programa() #usado para teste unitarios