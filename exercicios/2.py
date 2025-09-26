digite = input("Informe um texto: ")
vogais = "AEIOU"

for letra in digite:
    if letra.upper() in vogais:
         
     print(letra, end="")
         
     print()
     
for numero in range(0,5):
    print(numero, end=" ")