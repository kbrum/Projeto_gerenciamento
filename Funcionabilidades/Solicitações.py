from Funcionabilidades.Funções_basicas import Funções_basicas
from Funcionabilidades.Formatadores import Formatar

class Solicitar:
    def solicitar_entrada(mensagem, tipo):  # Função para garantir que a entrada não esteja em branco
                                            #faz checagem de entrada nula/vazia nos inputs
        while True:
            valor = input(f'\n{mensagem}\n------------->').strip()
            if valor:
                return valor
            else:
                Funções_basicas.limpar_tela()
                print(f'\nO {tipo} do seu produto não pode ficar em branco.')


    def solicitar_valor_conta():  # Função para garantir que o preço seja numérico
        while True:               #pergunta o valor da conta a ser cadastrada
            try:
                print('\nQual o valor da sua conta? (Insira apenas números)')
                preço = float(input('\n------------->').strip())
                if preço > 0:
                    return preço
                else:
                    Funções_basicas.limpar_tela()
                    print('O valor do produto deve ser positivo.')
            except ValueError:
                Funções_basicas.limpar_tela()
                Funções_basicas.preço_erro()
    
    def solicitar_dados(quem_chama): # Solicita o cpf ou cnpj de quem vai ser pago ou vai pagar
        while True:
            try:
                dado = None # onde fica armazenado se alguem esta pagando ou sendo pago
                if quem_chama == 'Contas_a_pagar': # se for chamado pelo contas a pagar
                    dado = 'recebedor'
                
                elif quem_chama == 'Contas_a_receber': # se for chamado pelo contas a receber
                    dado = 'paganete'
                
                print(f'\nDigite o CPF ou CNPJ do {dado}')
                dados = input('\n------------->').strip()
                if len(dados) == 11:
                    dados = Formatar.formatar_cpf(dados)
                    break
                elif len(dados) == 14:
                    dados = Formatar.formatar_cnpj(dados)
                    break
                else:
                    raise ValueError("CPF/CNPJ inválido.")
            except ValueError as e:
                print(f"\nErro: {e}. Não foi possível formatar o CPF/CNPJ.")