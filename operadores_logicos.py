
saldo = 10000
saque = 2500
limite = 4000
conta_especial = True

ex = saldo >= saque and saque <= limite or conta_especial and saldo >= saque 

ex2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque 
)

print(ex)

print(ex2)

conta_normal_com_saldo_suficiente =  saldo >= saque and saque <= limite 

conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque 

ex3 = conta_especial_com_saldo_suficiente or conta_normal_com_saldo_suficiente

print(ex3)