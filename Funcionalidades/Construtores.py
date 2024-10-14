
class Nova_conta: # objeto conta
        def __init__(self,nome,tipo,dado,valor,data,codigo,status): #contrutor de uma nova conta
            self.nome = nome
            self.tipo = tipo
            self.dado = dado
            self.valor = valor
            self.codigo = codigo
            self.status = status
            self.data = data
                
class Novo_funcionario: # objeto funcionario
        def __init__(self,nome,setor,posicao,codigo,status): #contrutor de uma nova conta
            self.nome = nome
            self.setor = setor
            self.posicao = posicao
            self.codigo = codigo
            self.status = status
            
class Novo_produto: # objeto produto
        def __init__(self,nome,tipo,subsecao,quantidade,valor,codigo):
            self.nome = nome
            self.tipo = tipo
            self.subsecao = subsecao
            self.quantidade = quantidade
            self.valor = valor
            self.codigo = codigo
            
class Novo_pedido: # objeto pedido
        def __init__(self,nome,seçao,tipo,quantidade,contato,valor,pagamento,codigo,status): #construtor de um novo pedido
            self.nome = nome
            self.seçao = seçao
            self.tipo = tipo
            self.quantidade = quantidade
            self.contato = contato
            self.valor = valor
            self.pagamento = pagamento
            self.codigo = codigo
            self.status = status