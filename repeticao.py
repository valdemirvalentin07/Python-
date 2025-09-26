texto = input("Informe um texto: ")
Vogais = "AEIOU"

for letra in texto:
    if letra.upper() in Vogais:
        print(letra, end="")
        
        print()
    
for numero in range(0,11):
    print(numero,end="")
    
    print()
#Exibindo a tabuada do 5
for numero in range(0, 81, 8):#Números foram alterados
    print(numero,end="  ")
    
#51 é exclusivo não inclusivo