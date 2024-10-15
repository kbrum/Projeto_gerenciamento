from Funcionalidades.Utils import *
from Funcionalidades.Geradorores import *
from Funcionalidades.Solicitações import *
from Funcionalidades.Construtores import Novo_funcionario
class Funcionarios: #Funcionarios
    def name_app():
        print('''
    ███████╗░██████╗░██╗░░░██╗██╗██████╗░███████╗
    ██╔════╝██╔═══██╗██║░░░██║██║██╔══██╗██╔════╝
    █████╗░░██║██╗██║██║░░░██║██║██████╔╝█████╗░░
    ██╔══╝░░╚██████╔╝██║░░░██║██║██╔═══╝░██╔══╝░░
    ███████╗░╚═██╔═╝░╚██████╔╝██║██║░░░░░███████╗
    ╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝╚═╝░░░░░╚══════╝''')

    gerador = Codigo() #instacia do gerador de codigo

    lista_funcionarios = []

    def cadastrar_funcionario():  # Função para cadastrar um novo funcionário
        while True:
            try:
                nome = solicitar_entrada('Qual o nome do seu funcionario?', 'nome', Funcionarios).upper()
                setor = solicitar_entrada('Qual o setor do seu funcionario?', 'setor', Funcionarios).upper()
                posicao = solicitar_entrada('Qual a posição desse funcionario? (ex: Analista, Tecnico, Estagiarios)', 'posição', Funcionarios)
                codigo = Funcionarios.gerador.pro_num()
                status = True
                
                # Armazena o novo funcionário
                funcionario_di = Novo_funcionario(nome,setor,posicao,codigo,status)
                Funcionarios.lista_funcionarios.append(funcionario_di)

                cadastro_feito(Funcionarios)  # Função para notificar que o cadastro foi feito
                break

            except Exception as e:
                limpar_tela()
                Funcionarios.name_app()
                print(f'\nErro: {e}')
                print('\nEste campo não pode ficar em branco.')

    def mostrar_funcionarios():  # Função para mostrar os funcionários cadastrados
        if len(Funcionarios.lista_funcionarios) == 0:
            print('\nNenhum funcioanrio cadastrado.')
        
        else:
            print('\nSeus funcionários são:')
            for funcionario in Funcionarios.lista_funcionarios:
                status_funcionarios = 'Ativo' if funcionario.status else 'desligado'    
                print(f'\n--> Nome: {funcionario.nome} | Setor: {funcionario.setor} | Posição: {funcionario.posicao} | Código: {funcionario.codigo} | Status do contrato: {status_funcionarios}')
            input('\n(Digite Enter para continuar)')

    def mostrar_opcoes(): #mostra as opçoes que o usuario pode escolher
        print('\n1 - Todos os funcionarios')
        print('2 - Cadastrar funcionario')
        print('3 - Voltar ao menu principal')

    def checagem():  # Checa a escolha que o usuário fez
        while True:
            try:
                print('\nEscolha uma opção')
                
                # Captura a entrada e remove espaços em branco
                escolha = input('\n-------------> ').strip()

                # Verifica se a entrada está vazia
                if not escolha:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.mostrar_opcoes_funcionarios()
                    print('\nA escolha não pode ficar em branco.')
                    continue 

                # Tenta converter para número inteiro
                escolha = int(escolha)

                # Verifica as opções
                if escolha == 1:
                    limpar_tela()
                    Funcionarios.name_app()
                    Funcionarios.mostrar_funcionarios()
                    Funcionarios.executar_programa()
                    break

                elif escolha == 2:
                    Funcionarios.cadastrar_funcionario()
                    cadastrar_outro(Funcionarios)
                    Funcionarios.executar_programa()
                    break
                
                else:
                    limpar_tela()
                    break

            except ValueError:  # Captura erros de conversão de string para int
                limpar_tela()
                Funcionarios.name_app()
                Funcionarios.mostrar_opcoes()
                erro_de_valor()     
        
    def executar_programa(): #executa o programa
        limpar_tela()
        Funcionarios.name_app()
        Funcionarios.mostrar_opcoes()
        Funcionarios.checagem()

#Funcionarios.executar_programa() #usado para teste unitarios