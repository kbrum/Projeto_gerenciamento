import os

class Funções_basicas:
    def variavel_em_branco(): #caso o usuario na digite nada
        print('\nEste campo não pode ficar em branco')

    def preço_erro(): #erro de preço de produto
        print('\n Insira um Preço valido(APENAS NUMEROS)')

    def erro_de_valor(): # aparece quando se digita algo que não é numero
        print('\nPor favor, selecione uma opção valida\n')

    def limpar_tela(): #Meio óbvio...
        os.system('cls')