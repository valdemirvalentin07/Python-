# Lidando com números
numero1 = 10 # tipo inteiro
numero2 = 5.6 # tipo float
numero3 = 5 + 2j
'''
There are three distinct numeric types: 
integers, floating-point numbers, 
and complex numbers.
'''
numero4 = int(numero2)
isinstance(numero1,object) # True
isinstance(numero1,int) # True
isinstance(numero1,float) # False

isinstance(numero2,object) # True
isinstance(numero2,int) # False
isinstance(numero2,float) # True

isinstance(numero3,object) # True
isinstance(numero3,int) # False
isinstance(numero3,float) # False
#######################################
# Faça um programa que receba dois números inteiros 
# e realize a soma dos dois números
valor1 = input('Digite o primeiro número: ')
valor1 = int(valor1)

valor2 = int(input('Digite o segundo número: '))

valor3 = valor1 + valor2
print(valor3)
#######################################
'''
Textual data in Python is handled with 
str objects, or strings. 
Strings are immutable sequences 
of Unicode code points. 
'''
s = 'Fatec Araras'
print(s.upper())

# Strings são iteráveis.

###########################################
# Dada uma string s, mostrar True caso a string tenha
# pelo menos uma vogal (a,e,i,o,u)
s1 = 'swtr' # False
s2 = 'oi mundo' # True

resultado_s1 = False
for letra in s1:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        resultado_s1 = True
print(resultado_s1)

resultado_s2 = False
for letra in s2:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        resultado_s2 = True
print(resultado_s2)

'''
Lists are mutable sequences, typically 
used to store collections of homogeneous 
items (where the precise degree of similarity 
will vary by application).
'''
lista = []
lista.append('batata')
lista.append('arroz')
lista.append('pão')
for x in range(3):
    lista.append(x)

print(lista)
# Percorrer a lista acima e mostrar apenas os itens de mercado
# ignorar os números
print(30 * '*')
for item in lista:
    if isinstance(item, str):
        print(item)

print(30 * '*')
for item in lista:
    if type(item) is str:
        print(item)

print(30 * '*')
for item in lista:
    x = str(item)
    if not x.isnumeric():
        print(x)

'''

Tuples are immutable sequences, 
typically used to store collections 
of heterogeneous data
'''
registro = ('Fatec','Araras')
type(registro)

lista.append('batata')
lista.append('arroz')
lista.append('pão')
lista.append('arroz')

print(lista)
# ['batata', 'arroz', 'pão', 0, 1, 2, 'batata', 'arroz', 'pão', 'arroz']
# Remover todos os elementos duplicados da lista acima
l1 = []
for x in lista:
    if not x in l1:
        l1.append(x)

l2 = list(set(lista)) # Fiz uso da estrutura set (conjunto)
conjunto1 = set(range(1,10))
conjunto1
#{1,2,3,4,5,6,7,8,9,}
conjunto2 = set(range(6,16))
#{6,7,8,9,10,11,12,13,14,15}
#conjunto1.intersection(conjunto2)
#{8,9,6,7}
conjunto3 = set(range(7,10))

conjunto4 = set([11,12])

for elemento in conjunto1:
    print(elemento)
    
conjunto3.issubset(conjunto2)#true
conjunto3.issubset(conjunto1)#true
conjunto4.issubset(conjunto2)#true
conjunto4.issubset(conjunto1)#true

conjunto1.union(conjunto2)# (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
conjunto2.difference(conjunto1)#{10,11,12,13,14,15}
conjunto1.difference(conjunto2)#{1,2,3,4,5,}
conjunto1.intersection(conjunto2)#{8,9,6,7}

print = conjunto1.union(conjunto2)
print = conjunto2.difference(conjunto1)
print = conjunto1.difference(conjunto2)
print = conjunto1.intersection(conjunto2)

fatec = {}
fatec['Orlando'] = 'DW3'
fatec['Edras'] = 'Técnicas de Programação 2'


fatec ['fabio'] = ['Algebra Linear']

fatec.keys()

list(fatec.keys())

list(fatec.values())

'orlando' in fatec

fatec.get('orlando')
fatec.get('Orlando')
fatec.get('Aulavaga','Não tenho esse professor')

fatec.get('orlando','Não tenho esse professor')

print(fatec)