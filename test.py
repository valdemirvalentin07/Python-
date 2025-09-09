class Escritorio:
    def __init__(self, funcionario, cliente):
        self.funcionario = funcionario
        self.cliente = cliente 
        
    def recebe_cliente(self):
        print(f"Cliente {self.cliente} recebido por {self.funcionario}")
    
    def contratacao(self):
        print(f"Contratação efetivada entre {self.funcionario} e {self.cliente}")
        
    def __str__(self):
        return f"{self.funcionario} atende {self.cliente}"


class Contrato:
    def __init__(self):
        self.funcionarios_nome = ['Paulo','José','Lucas','Matheus']
        self.clientes_nome = ['AmazonPrime','Pinterest','Google','Netflix','HBOmax']
        
        # cria combinações funcionário x cliente
        self.contratacoes = [
            Escritorio(funcionario, cliente) 
            for funcionario in self.funcionarios_nome 
            for cliente in self.clientes_nome
        ]

contratos = Contrato()

# pegar uma contratação e ver como funciona
exemplo = contratos.contratacoes[0]  
print(exemplo)                # Paulo atende AmazonPrime
exemplo.recebe_cliente()      # Cliente AmazonPrime recebido por Paulo
exemplo.contratacao()         # Contratação efetivada entre Paulo e AmazonPrime
