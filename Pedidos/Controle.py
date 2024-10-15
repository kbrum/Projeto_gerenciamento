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
                    nome = solicitar_entrada('Qual o nome do cliente que está fazendo o pedido?', 'nome', quem_chama)
                    seçao = solicitar_seçao(quem_chama)
                    tipo = solicitar_entrada('Qual o tipo do seu pedido? (ex: Bolo, Centro de salgado)', 'tipo', quem_chama)
                    quantidade = solicitar_quantidade(quem_chama)
                    numero = solicitar_numero()
                    valor = solicitar_valor(quem_chama_str)
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
                    
    def finalizar_pedido(quem_chama, quem_chama_str): # Solicita ao usuário o código do pedido para finalizar
        while True:
            try:
                limpar_tela()
                quem_chama.name_app()
                codigo = int(input('\nDigite o código do pedido que deseja finalizar: ').strip())
                
                if quem_chama_str == 'Seção de doces': # se for chamado na seção de doces
                    pedido_encontrada = None
                    for pedido in Controle_pedido.pedidos_doces: # procurando o codigo na lista de pedidos doces
                        if pedido.codigo == codigo:
                            pedido_encontrada == pedido
                        
                        else:
                            print(f'\npedido de código {codigo} não encontrada.') #caso a pedido não seja encontrado
                    if pedido.status == True:
                        pedido.status = False
                        limpar_tela()
                        quem_chama.name_app()
                        print(f'\nO pedido "{pedido.tipo}" do cliente "{pedido.nome}" de código {pedido.codigo} {'ainda esta Pendente' if pedido.status else 'foi Finalizado com sucesso'}')
                        
                        input('\n(Pressione Enter para continuar)')
                        break
                    
                elif quem_chama_str == 'Seção de salgados': # se for chamado na seção de salgados
                    pedido_encontrada = None
                    for pedido in Controle_pedido.pedidos_salgados: # procurando o codigo na lista de pedidos salgados
                        if pedido.codigo == codigo:
                            pedido_encontrada == pedido
                        
                        else:
                            print(f'\npedido de código {codigo} não encontrada.') #caso a pedido não seja encontrado
                    if pedido.status == True:
                        pedido.status = False
                        limpar_tela()
                        quem_chama.name_app()
                        print(f'\nA pedido "{pedido.nome}" de código {pedido.codigo} {'ainda esta Pendente' if pedido.status else 'foi Paga com sucesso'}')
                        
                        input('\n(Pressione Enter para continuar)')
                        break
                	
            except ValueError:
                print('Erro: O código da pedido deve ser um número inteiro.') # caso digite uma letra ou deixe vazio