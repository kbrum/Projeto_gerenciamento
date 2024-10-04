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
    

def Conferir_alternativas():
    
    escolher_opcoes = int(input('Escolha uma opção: '))
            
    if escolher_opcoes == 1:
        os.system('cls')
        main_produtos()
                
    elif escolher_opcoes == 2:
        os.system('cls')
        main_estoque()
                
    elif escolher_opcoes == 3:
        os.system('cls')
        main_financeiro()
                
    elif escolher_opcoes == 4:
        os.system('cls')
        main_funcionarios()
                
    elif escolher_opcoes == 5:
        os.system('cls')
        print('Finalizado')
            
    elif escolher_opcoes != int:
        print('Digite apenas numeros')
            
    else:
        print("Por favor, selecione uma opção valida")
        
        
def main():
    name_app()
    exibir_opcoes()
    Conferir_alternativas()
    

main()