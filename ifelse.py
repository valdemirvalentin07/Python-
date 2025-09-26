maior_idade = 18
idade_especial = 17

idade = int(input("Infome sua idade: "))

if idade >= maior_idade: 
    print("Maior de idade, pode tirar a habilitação.")
elif idade < maior_idade: 
    print( "Você não pode tirar a habilitação.")
    
    
if idade >= maior_idade: 
    print("Maior de idade, pode tirar a habilitação.")

elif idade <= idade_especial:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas.")   

else:  
    print( "Você não pode tirar a habilitação.")
    
