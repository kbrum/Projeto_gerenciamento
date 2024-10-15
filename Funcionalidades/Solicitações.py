from .Utils import *
from .Formatadores import *
from datetime import datetime

def solicitar_entrada(mensagem, tipo, quem_chama):  # Faz checagem de entrada nula/vazia nos inputs+                                 
    while True:
        limpar_tela()
        quem_chama.name_app()
        valor = input(f'\n{mensagem}\n------------->').strip()
        if valor:
            return valor
        else:
            quem_chama.name_app()
            limpar_tela()
            print(f'\nO {tipo} do seu produto não pode ficar em branco.')

def solicitar_valor(quem_chama,quem_chama_str):  # Solicita o valor da conta a ser cadastrada
    while True:        
        try:
            limpar_tela()
            quem_chama.name_app()
            dado = None
            if quem_chama_str ==  'Contas_a_pagar' or quem_chama_str == 'Contas_a_receber':
                dado = 'da sua conta?'
            
            elif quem_chama_str == 'Produtos':
                dado = 'do seu produto?'
                
            elif quem_chama_str == 'Pedidos':
                dado = 'do seu pedido?'
            
            print(f'\nQual o valor {dado} (Insira apenas números)')
            valor = float(input('\n------------->').strip())
            if valor > 0: # Função para garantir que o valor seja numérico
                return valor
            else:
                limpar_tela()
                print(f'O valor {dado} deve ser positivo.')
        except ValueError:
            limpar_tela()
            preço_erro()
            
def solicitar_dados(quem_chama,quem_chama_str): # Solicita o cpf ou cnpj de quem vai ser pago ou vai pagar
    while True:
        try:
            limpar_tela()
            quem_chama.name_app()
            dado = None # onde fica armazenado se alguem esta pagando ou sendo pago
            if quem_chama == 'Contas_a_pagar': # se for chamado pelo contas a pagar
                dado = 'recebedor'
            
            elif quem_chama_str == 'Contas_a_receber': # se for chamado pelo contas a receber
                dado = 'pagante'
            
            print(f'\nDigite o CPF ou CNPJ do {dado}')
            dados = input('\n------------->').strip()
            if len(dados) == 11:
                dados = formatar_cpf(dados)
                break
            elif len(dados) == 14:
                dados = formatar_cnpj(dados)
                break
            else:
                raise ValueError("CPF/CNPJ inválido.")
        except ValueError as e:
            print(f"\nErro: {e}. Não foi possível formatar o CPF/CNPJ.")
    
    return dados

def solicitar_data(quem_chama,quem_chama_str): # Solicita a data
    while True:
        limpar_tela()
        quem_chama.name_app()
        dado = None # variavel vazia para guardar que modulo chamou a funçao
        if quem_chama_str == 'Contas_a_pagar' or quem_chama_str == 'Contas_a_receber':
            dado = 'de abertura da conta'
            
        data = input(f'\nDigite a data {dado}: (dd/mm/aaaa): ').strip()
        try:
            if len(data) == 10:
                # Tenta converter a string em uma data
                data_final = datetime.strptime(data, '%d/%m/%Y')
                break
            
            else:
                print('\nData inválida. Tente novamente.')

        except ValueError as e:
            print(f'Error: {e}')

    return data_final

def solicitar_quantidade(quem_chama): #solicita a quantidade de produtos em estoque
    while True:
        try:
            limpar_tela()
            quem_chama.name_app()
            print('\nQual a quantidade do seu produto? (Insira apenas números)')
            preço = int(input('\n------------->').strip())
            if preço > 0:
                return preço
            else:
                limpar_tela()
                quem_chama.name_app()
                print('A quantidade do produto deve ser positiva.')
        except ValueError:
            limpar_tela()
            quem_chama.name_app()
            preço_erro()
                
def solicitar_pagamento(quem_chama): #Pergunta a forma de pagamento
    while True:
        try:
            limpar_tela()
            quem_chama.name_app()
            print('\nQual a forma de pagamento? ')
            print('1 - Cartão de Débito')
            print('2 - Cartão de Crédito')
            print('3 - Pix')
            
            pagamento = input('\n-------------> ').strip()
            
            if not pagamento: # verifica se a entrada do pagamento não é vazia
                limpar_tela()
                quem_chama.name_app()
                print('\nEste campo não pode ficar em branco')
                input('\n(Digite Enter para continuar)')
                continue
            
            pagamento = int(pagamento)
            
            if pagamento == 1: # pagar com debito
                limpar_tela()
                pagamento = 'Cartão de Débito'
                break
            
            elif pagamento == 2: # pagar com credito
                limpar_tela()
                pagamento = 'Cartão Crédito'
                break
            
            elif pagamento == 3: # pagar com pix
                limpar_tela()
                pagamento = 'Pix'
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            limpar_tela()
            quem_chama.name_app()
            erro_de_valor()
            input('\n(Digite Enter para continuar)')

    return pagamento
        
def solicitar_numero(quem_chama): # solicta um numero para contato
    while True:
        try:
            limpar_tela()
            quem_chama.name_app()
            print('\nDigite um numero para contato (com DDD)')
            numero = input('\n------------->').strip()
            if len(numero) == 11:
                numero = formatar_numero(numero)
                break
            else:
                raise ValueError("Numero inválido.")
        except ValueError as e:
            print(f"\nErro: {e}. Não foi possível formatar o numero.")
    
    return numero

def solicitar_seçao(quem_chama):
    while True:
        try:
            limpar_tela()
            quem_chama.name_app()
            limpar_tela()
            quem_chama.name_app()
            print('\nDe qual seção você deseja pedir? ')
            print('1 - Seção de doces')
            print('2 - Seção de salgados')
            
            seçao = input('\n-------------> ').strip()
            
            if not seçao: # verifica se a entrada do seçao não é vazia
                limpar_tela()
                quem_chama.name_app()
                print('\nEste campo não pode ficar em branco')
                input('\n(Digite Enter para continuar)')
                continue
            
            seçao = int(seçao)
            
            if seçao == 1: # seção de doces
                limpar_tela()
                seçao = 'Seção de doces'
                break
            
            elif seçao == 2: # seção de salgados
                limpar_tela()
                seçao = 'Seção de salgados'
                break
            
        except ValueError: #em caso de inserir algo que não é numero na opção
            limpar_tela()
            quem_chama.name_app()
            erro_de_valor()
            input('\n(Digite Enter para continuar)')
    return seçao
# o parametro quem_chama serve para identificar de qual setor a função esta sendo chamada para poder exibir as funçoes "name_app" corretamente