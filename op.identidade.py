curso = "Curso de Python"
nome_curso = curso 
saldo, limite = 200, 200

a = curso is nome_curso

b = curso is not nome_curso

c = saldo is limite 

print(a , b , c)

saldo = 1000
limite = 1000

print( saldo is limite)
print(saldo is not limite)