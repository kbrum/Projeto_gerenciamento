from .Utils import *
from .Formatadores import *
from datetime import datetime

def solicitar_entrada(mensagem, tipo, quem_chama):  # Faz checagem de entrada nula/vazia nos inputs+
                                        
    while True:
        valor = input(f'\n{mensagem}\n------------->').strip()
        if valor:
            return valor
        else:
            quem_chama.name_app
            limpar_tela()
            print(f'\nO {tipo} do seu produto não pode ficar em branco.')

def solicitar_valor_conta():  # Solicita o valor da conta a ser cadastrada
    while True:        
        try:
            print('\nQual o valor da sua conta? (Insira apenas números)')
            preço = float(input('\n------------->').strip())
            if preço > 0: # Função para garantir que o preço seja numérico
                return preço
            else:
                limpar_tela()
                print('O valor do produto deve ser positivo.')
        except ValueError:
            limpar_tela()
            preço_erro()
            
def solicitar_dados(quem_chama): # Solicita o cpf ou cnpj de quem vai ser pago ou vai pagar
    while True:
        try:
            dado = None # onde fica armazenado se alguem esta pagando ou sendo pago
            if quem_chama == 'Contas_a_pagar': # se for chamado pelo contas a pagar
                dado = 'recebedor'
            
            elif quem_chama == 'Contas_a_receber': # se for chamado pelo contas a receber
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

def solicitar_data(quem_chama): # Solicita a data
    while True:
        dado = None # variavel vazia para guardar que modulo chamou a funçao
        if quem_chama == 'Contas_a_pagar' or quem_chama == 'Contas_a_receber':
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

