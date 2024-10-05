import os
from Produtos import *
from Estoque import *
from Funcionarios import * 
from Financeiro import *

def name_app():     
    print('''
░██████╗░███████╗██████╗░███████╗███╗░░██╗░█████╗░██╗░█████╗░
██╔════╝░██╔════╝██╔══██╗██╔════╝████╗░██║██╔══██╗██║██╔══██╗
██║░░██╗░█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░╚═╝██║███████║
██║░░╚██╗██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░██╗██║██╔══██║
╚██████╔╝███████╗██║░░██║███████╗██║░╚███║╚█████╔╝██║██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░╚═╝''')
   
    
def exibir_opcoes():
    print('Seja bem vindo')
    print('1 - Produtos')
    print('2 - Estoque')
    print('3 - Gerenciamento Financeiro')
    print('4 - Funcionarios')
    print('5 - Sair')
    

def erro_de_valor():
    print("Por favor, selecione uma opção valida\n")


def Conferir_alternativas():
    while True:
        try:
            escolher_opcoes = int(input('Escolha uma opção: '))
                    
            if escolher_opcoes == 1:
                os.system('cls')
                main_produtos()
                break
                        
            elif escolher_opcoes == 2:
                os.system('cls')
                main_estoque()
                break
                        
            elif escolher_opcoes == 3:
                os.system('cls')
                main_financeiro()
                break
                        
            elif escolher_opcoes == 4:
                os.system('cls')
                main_funcionarios()
                break
                        
            elif escolher_opcoes == 5:
                os.system('cls')
                print('Finalizado')
                break
                    
            else:
                erro_de_valor()
        except:
            erro_de_valor()
        
def main():
    os.system('cls')
    name_app()
    exibir_opcoes()
    Conferir_alternativas()
    

main()