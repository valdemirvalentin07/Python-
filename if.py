saldo = 1300

saque =250

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")