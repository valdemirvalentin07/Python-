nome = "Gahlego"
idade = 23
profissao = "Programador"
linguagem = "Python"
saldo = 12.444

dados = {"nome": "Gahlego", "idade": 23 }

print("nome: %s Idade: %d" % (nome,idade))

print("Nome: {1} Idade: {0} Nome: {1} Nome: {1}".format(idade,nome))

print("Nome: {} Idade: {}".format(idade,nome))

print("Nome: {name} Idade: {age}".format(age= idade, name= nome))

print("Nome: {nome} Idade: {idade}".format(idade= idade, nome= nome))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")

print(f"Nome: {nome} Idade: {idade} saldo: {saldo:2f}")

print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}")

nome[0]
