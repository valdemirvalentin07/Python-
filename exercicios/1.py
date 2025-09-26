  
  
print("Bem-vindo a nossa agência bancária!")

consultar_saldo = 3000
deposito = 0.0
saque = 0.0

opcao = -1 

while opcao != 0:
    
    print(35 * "*")
    
    opcao = int (input("[1]Fazer depósito\n[2]Consultar Saldo\n[3]Saque\n[0]Sair\n:"))
    
      
    if opcao == 1:
       deposito = float(input(f"Digite o valor do depósito:\n "))
       consultar_saldo += deposito
       print(f"Você depositou R$ {deposito}\n")
        
        
    elif opcao == 2:
        print(f"seu saldo é de R$ {consultar_saldo}\n")
        
             
    elif opcao == 3:
        saque= float(input("Digite valor do saque:\n"))
        if saque <= consultar_saldo:
         consultar_saldo -= saque 
         print(f"Sacou: R${saque}\n")
         
        else: 
         print("Saldo insuficiente, consulte seu saldo e tente novamente!\n")
        
    elif opcao == 0:
          print("Obrigado por usar nosso sistema bancário, até logo!\n")
  
           
    else: 
           print("Opção inválida, tente novamente!\n")