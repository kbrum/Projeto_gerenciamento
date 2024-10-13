
def formatar_cpf(cpf): #formata um cpf
        cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere que não seja dígito
        if len(cpf) != 11:
                raise ValueError("O CPF deve ter 11 dígitos.")
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def formatar_cnpj(cnpj): #formata um cnpj
        cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove qualquer caractere que não seja dígito
        if len(cnpj) != 14:
                raise ValueError("O CNPJ deve ter 14 dígitos.")
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'

def formatar_numero(numero): #formata um numero de telefone
        numero = ''.join(filter(str.isdigit, numero))  # Remove qualquer caractere que não seja dígito
        if len(numero) != 11:
            raise ValueError("O numero deve ter 11 dígitos.")
        return f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'