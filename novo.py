list = []
list.append('Batata')
list.append('Arroz')
list.append('Feijão')
list.append('Alface')
for x in range (4):
     list.append(x)
     print(list)
      
print(30 * '*')
for item in list: 
        if isinstance(item,str):
         print(item)