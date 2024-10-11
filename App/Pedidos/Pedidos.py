from App.Funcionabilidades.Funções_basicas import Funções_basicas

class codigo: #gera um codigo de pedido autoincrementavel
        def __init__(self):
            self.codigo = 0
            
        def pro_num(self):
            self.codigo +=1
            return self.codigo

class Pedidos: #Pedidos
    def name_app():
        print('''
    ██████╗░███████╗██████╗░██╗██████╗░░█████╗░░██████╗
    ██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝
    ██████╔╝█████╗░░██║░░██║██║██║░░██║██║░░██║╚█████╗░
    ██╔═══╝░██╔══╝░░██║░░██║██║██║░░██║██║░░██║░╚═══██╗
    ██║░░░░░███████╗██████╔╝██║██████╔╝╚█████╔╝██████╔╝
    ╚═╝░░░░░╚══════╝╚═════╝░╚═╝╚═════╝░░╚════╝░╚═════╝░         
              ''')
        
    class Pedido: #obejto pedido
        def __init__(self,nome,tipo,quantidade,contato,valor,pagamento,codigo,status): #construtor de um novo pedido
            self.nome = nome
            self.tipo = tipo
            self.quantidade = quantidade
            self.contato = contato
            self.valor = valor
            self.pagamento = pagamento
            self.codigo = codigo
            self.status = status
        
        def finalizar_pedido(self): # finalizador de pedidos (altera o self.status de true para false ('pedido ativo/pedido finalizado'))
            if self.status:  # Verifica se o pedido está ativo
                self.status = False
                print(f"Pedido {self.codigo} finalizado.")
            else:
                print(f"Pedido {self.codigo} já está finalizado.")
        
    gerador = codigo() #instacia do gerador de codigo
    
    class FazerPedido: # para fazer um novo pedido
        
        def solicitar_valor():  # Função para garantir que o preço seja numérico
            while True:
                try:
                    print('\nQual o valor do seu pedido? (Insira apenas números)')
                    valor = float(input('\n------------->').strip())
                    if valor > 0:
                        return valor
                    else:
                        Funções_basicas.limpar_tela()
                        Pedidos.name_app()
                        print('O valor do pedido deve ser positivo.')
                except ValueError:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Funções_basicas.preço_erro()
        
        def solicitar_pagamento(): #Pergunta a forma de pagamento
            while True:
                try:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    print('\nQual a forma de pagamento? ')
                    print('1 - Cartão de Débito')
                    print('2 - Cartão de Crédito')
                    print('3 - Pix')
                    
                    pagamento = input('\n-------------> ').strip()
                    
                    if not pagamento: # verifica se a entrada do pagamento não é vazia
                        Funções_basicas.limpar_tela()
                        Pedidos.name_app()
                        print('\nEste campo não pode ficar em branco')
                        input('\n(Digite Enter para continuar)')
                        continue
                    
                    pagamento = int(pagamento)
                    
                    if pagamento == 1: # pagar com debito
                        Funções_basicas.limpar_tela()
                        pagamento = 'Cartão de Débito'
                        break
                    
                    elif pagamento == 2: # pagar com credito
                        Funções_basicas.limpar_tela()
                        pagamento = 'Cartão Crédito'
                        break
                    
                    elif pagamento == 3: # pagar com pix
                        Funções_basicas.limpar_tela()
                        pagamento = 'Pix'
                        break
                    
                except ValueError: #em caso de inserir algo que não é numero na opção
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Funções_basicas.erro_de_valor()
                    input('\n(Digite Enter para continuar)')
 
            return pagamento

        def solicitar_quantidade(): #solicita a quantidade de produtos em estoque
            while True:
                try:
                    print('\nQual a quantidade de itens no pedido? (Insira apenas números)')
                    preço = int(input('\n------------->').strip())
                    if preço > 0:
                        return preço
                    else:
                        Funções_basicas.limpar_tela()
                        Pedidos.name_app()
                        print('A quantidade do produto deve ser positiva.')
                except ValueError:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Funções_basicas.preço_erro()
    
        def solicitar_numero(): # solicta um numero para contato
                while True:
                    try:
                        print('\nDigite um numero para contato (com DDD)')
                        numero = input('\n------------->').strip()
                        if len(numero) == 11:
                            numero = Pedidos.formatar_numero(numero)
                            break
                        else:
                            raise ValueError("Numero inválido.")
                    except ValueError as e:
                        print(f"\nErro: {e}. Não foi possível formatar o numero.")
                
                return numero
            
        def pedido_feito(): #mostra mensagem de pedido bem sucedido
            Funções_basicas.limpar_tela()
            Pedidos.name_app()
            print('\n Um codigo de identificação foi gerado automaticamente a seu Pedido')
            print('\n Pedido realizado com succeso')
            input('\n Pressione enter para continuar')
        
        pedidos = []
    
        def cadastrar_pedido():  # Função para cadastrar um novo produto
            while True:
                try:
                    nome = Pedidos.solicitar_entrada('Qual o nome de quem esta fazendo o pedido', 'nome')
                    tipo = Pedidos.solicitar_entrada('Qual o tipo do seu pedido? (ex: Bolo, Doces, Torta)', 'tipo')
                    quantidade = Pedidos.FazerPedido.solicitar_quantidade()
                    numero = Pedidos.FazerPedido.solicitar_numero()
                    valor = Pedidos.FazerPedido.solicitar_valor()
                    pagamento = Pedidos.FazerPedido.solicitar_pagamento()
                    codigo = Pedidos.gerador.pro_num()
                    status = True
                    
                    final = Pedidos.Pedido(nome,tipo,quantidade,numero,valor,pagamento,codigo,status)
                    
                    Pedidos.FazerPedido.pedidos.append(final)
                    
                    Pedidos.FazerPedido.pedido_feito()  # Confirma o cadastro do produto
                    break 

                except ValueError:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Funções_basicas.preço_erro()
                           
    def menu_pedidos(): #pergunta ao usuario se quer voltar ao menu financeiro
        while True:
            try:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                print('\nDeseja voltar ao menu? ')
                print('1 - Sim')
                print('2 - Não')
                
                menu = input('\n-------------> ').strip()
                
                if not menu: # verifica se a entrada do menu não é vazia
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    print('\nEste campo não pode ficar em branco')
                    input('\n(Digite Enter para continuar)')
                    continue
                
                menu = int(menu)
                
                if menu == 2: # fecha o programa
                    Funções_basicas.limpar_tela()
                    print('Finalizado')
                    break
                
                elif menu == 1: # volta ao menu de pedidos
                    Funções_basicas.limpar_tela()
                    Pedidos.main_pedidos()
                    break
                
            except ValueError: #em caso de inserir algo que não é numero na opção
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                Funções_basicas.erro_de_valor()
                input('\n(Digite Enter para continuar)')
    
    def formatar_numero(numero): #formata um numero
        numero = ''.join(filter(str.isdigit, numero))  # Remove qualquer caractere que não seja dígito
        if len(numero) != 11:
            raise ValueError("O numero deve ter 11 dígitos.")
        return f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'
    
    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                print(f'\nO {tipo} do seu produto não pode ficar em branco.')  
    
    def mostrar_todos(): #mostra todos os pedidos ja feitos
        if len(Pedidos.FazerPedido.pedidos) == 0: # checa se a lista esta vazia
            print('\nNenhum pedido cadastrado.')
        else:
            print('\nLista de pedidos feitos:')
            for i, pedido in enumerate(Pedidos.FazerPedido.pedidos, start=1):
                status_pedido = 'Pedido ativo' if pedido.status else 'Pedido finalizado' # Fatora a string para exibir pedido ativo ou finalizado em vez de true ou false
                print(f'\n{i}. Nome: {pedido.nome} | Tipo: {pedido.tipo} | Quantidade: {pedido.quantidade} | Numero para contato: {pedido.contato} | Valor do pedido: R${pedido.valor} | Forma de pagamento: {pedido.pagamento} | Código: {pedido.codigo} | Status do pedido: {status_pedido}')
                #exibe na tela os pedidos
                
        input('\n(Digite Enter para continuar)')
    
    def mostrar_ativos(): #mostra apenas os pedidos ativos
        if len(Pedidos.FazerPedido.pedidos) == 0:
            print('\nNenhum pedido ativo ou cadastrado')
        else:
            print('\nLista de pedidos feitos:')
            for i, pedido in enumerate(Pedidos.FazerPedido.pedidos, start=1):
                status_pedido = 'Pedido ativo' if pedido.status else 'Pedido finalizado' # Fatora a string para exibir pedido ativo ou finalizado em vez de true ou false
                if status_pedido == 'Pedido ativo': # verifica se o pedido esta ativo ou finalizado
                    print(f'\n{i}. Nome: {pedido.nome} | Tipo: {pedido.tipo} | Quantidade: {pedido.quantidade} | Numero para contato: {pedido.contato} | Valor do pedido: R${pedido.valor} | Forma de pagamento: {pedido.pagamento} | Código: {pedido.codigo} | Status do pedido: {status_pedido}')
                else:
                    print('\nNenhum pedido ativo ou cadastrado')  

        input('\n(Digite Enter para continuar)')
        
    def alterar_status_pedido(): # Solicita ao usuário o código do pedido para finalizar
        while True:
            try:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                codigo = int(input('Digite o código do pedido que deseja finalizar: ').strip())
                
                # Busca o pedido com o código informado
                pedido_encontrado = None # gera uma variavel fazia para procurar o codigo na lista
                for pedido in Pedidos.FazerPedido.pedidos: # procurando o codigo na lista
                    if pedido.codigo == codigo:
                        pedido_encontrado = pedido # caso ele exista ele é alocado dentro da variavel 'pedido_encontrado'
                
                if pedido_encontrado:
                    pedido_encontrado.finalizar_pedido() # chama a função que finaliza pedidos
                    
                    print('\nStatus dos pedidos após alteração:') #informa que o pedido x foi finalizado com sucesso
                    for pedido in Pedidos.FazerPedido.pedidos:
                        Funções_basicas.limpar_tela()
                        Pedidos.name_app()
                        print(f'\nO pedido de código {pedido.codigo} foi {'Ativo' if pedido.status else 'Finalizado'} com sucesso') # mensagem de finalizado
                        
                    input('\n(Precione Enter para continuar)')
                    break
                
                else:
                    print(f'\nPedido com código {codigo} não encontrado.') #caso o pedido não seja encontrado
            
            except ValueError:
                print('Erro: O código do pedido deve ser um número inteiro.') # caso digite uma letra ou deixe vazio
  
    def mostrar_opcoes(): # mostra as oções que podem ser escolhidas
        print('\n1 - Ver todos os pedidos')
        print('2 - Ver pedidos ativos')
        print('3 - Fazer pedido')
        print('4 - Finalizar pedido')
        print('5 - Voltar ao menu principal')
    
    def checagem(): # checa a opção q o usuario escolheu
        while True:
            try:
                print('\nEscolha uma opção')
                escolha = int(input('\n-------------> '))
                
                if escolha == 1:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Pedidos.mostrar_todos()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha == 2:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Pedidos.mostrar_ativos()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha== 3:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Pedidos.FazerPedido.cadastrar_pedido()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha == 4:
                    Funções_basicas.limpar_tela()
                    Pedidos.name_app()
                    Pedidos.alterar_status_pedido()
                    Pedidos.menu_pedidos()
                    break
                
                elif escolha == 5:
                    Funções_basicas.limpar_tela()
                    Main.main()
                    break
            
            except ValueError:
                Funções_basicas.limpar_tela()
                Pedidos.name_app()
                Pedidos.mostrar_opcoes()
                Funções_basicas.erro_de_valor()
                Pedidos.checagem()
    
    def main_pedidos(): # executa as funçoes na ordem
        Funções_basicas.limpar_tela()
        Pedidos.name_app()
        Pedidos.mostrar_opcoes()
        Pedidos.checagem()
        
    def executar_programa(): # mostra na tela
        Pedidos.main_pedidos()

Pedidos.executar_programa() # usado para testes unitarios