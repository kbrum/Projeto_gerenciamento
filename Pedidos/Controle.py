from Funcionalidades.Utils import *
from Funcionalidades.Solicitações import *
from Funcionalidades.Geradorores import *
from Funcionalidades.Construtores import Novo_pedido

class Controle_pedido:
    gerador = Codigo() # instacia do gerador de codigo
    pedidos_doces = []
    pedidos_salgados = []
    
    def fazer_pedido(quem_chama, quem_chama_str):  #quem_chama se refere a classe que esta importando a função, quem_chama_str é apenas uma representação do nome dessam classe em formato de string
            while True:
                try: # Função para cadastrar um novo produto
                    nome = solicitar_entrada('Qual o nome do cliente que está fazendo o pedido?', 'nome', quem_chama).upper()
                    seçao = solicitar_seçao(quem_chama)
                    tipo = solicitar_entrada('Qual o tipo do seu pedido? (ex: Bolo, Centro de salgado)', 'tipo', quem_chama).upper()
                    quantidade = solicitar_quantidade(quem_chama)
                    numero = solicitar_numero(quem_chama)
                    valor = solicitar_valor(quem_chama_str,quem_chama)
                    pagamento = solicitar_pagamento(quem_chama)
                    codigo = Controle_pedido.gerador.pro_num()
                    status = True
                    
                    if seçao == 'Seção de doces':
                        final = Novo_pedido(nome,seçao,tipo,quantidade,numero,valor,pagamento,codigo,status)
                        Controle_pedido.pedidos_doces.append(final)
                        
                    elif seçao == 'Seção de salgados':
                        final = Novo_pedido(nome,seçao,tipo,quantidade,numero,valor,pagamento,codigo,status)
                        Controle_pedido.pedidos_salgados.append(final)
                        
                    cadastro_feito(quem_chama)# Confirma o cadastro do produto
                    break 

                except ValueError:
                    limpar_tela()
                    quem_chama.name_app()
                    preço_erro()
                    
    def finalizar_pedido_doce(quem_chama): # Solicita ao usuário o código do pedido para finalizar
        while True:
            try:
                limpar_tela()
                quem_chama.name_app()
                codigo_d = input('\nDigite o código do pedido que deseja finalizar: ').strip()
                
                codigo_d = int(codigo_d)
                
                pedido_encontrada = None  # Variável para armazenar o pedido encontrado
                for pedido in Controle_pedido.pedidos_doces:  # Procurando o código na lista de pedidos doces
                    if pedido.codigo == codigo_d:
                        pedido_encontrada = pedido
                        break 
                
                if pedido_encontrada:  # Se o pedido foi encontrado
                    if pedido_encontrada.status:  # Verifica se o pedido está pendente
                        pedido_encontrada.status = False  # Finaliza o pedido
                        limpar_tela()
                        quem_chama.name_app()
                        print(f'\nO pedido "{pedido_encontrada.tipo}" do cliente "{pedido_encontrada.nome}" '
                            f'de código {pedido_encontrada.codigo} foi finalizado com sucesso.')
                    else:
                        print(f'\nO pedido "{pedido_encontrada.tipo}" do cliente "{pedido_encontrada.nome}" '
                            f'de código {pedido_encontrada.codigo} já estava finalizado.')
                else:
                    print(f'\nPedido de código {codigo_d} não encontrado.')  # Mensagem caso o pedido não seja encontrado
                
                input('\n(Pressione Enter para continuar)')
                break  # Finaliza o loop
            
            except ValueError:
                print('\nErro: O código do pedido deve ser um número inteiro.')  # Caso digite uma letra ou deixe vazio
                input('\n(Pressione Enter para continuar)')
    
    def finalizar_pedido_salgado(quem_chama):
        while True:
            try:
                limpar_tela()
                quem_chama.name_app()
                codigo_s = input('\nDigite o código do pedido que deseja finalizar: ').strip()
                
                codigo_s = int(codigo_s)
                
                pedido_encontrada = None  # Variável para armazenar o pedido encontrado
                for pedido in Controle_pedido.pedidos_salgados:  # Procurando o código na lista de pedidos salgados
                    if pedido.codigo == codigo_s:
                        pedido_encontrada = pedido
                        break 
                
                if pedido_encontrada:  # Se o pedido foi encontrado
                    if pedido_encontrada.status:  # Verifica se o pedido está pendente
                        pedido_encontrada.status = False  # Finaliza o pedido
                        
                        limpar_tela()
                        quem_chama.name_app()
                        print(f'\nO pedido "{pedido_encontrada.nome}" de código {pedido_encontrada.codigo} foi finalizado com sucesso.')
                    else:
                        print(f'\nO pedido "{pedido_encontrada.nome}" de código {pedido_encontrada.codigo} já estava finalizado.')
                else:
                    print(f'\nPedido de código {codigo_s} não encontrado.')  # Caso o pedido não seja encontrado
                
                input('\n(Pressione Enter para continuar)')
                break 
            
            except ValueError:
                print('\nErro: O código do pedido deve ser um número.')  # Caso digite uma letra ou deixe vazio
                input('\n(Pressione Enter para continuar)')