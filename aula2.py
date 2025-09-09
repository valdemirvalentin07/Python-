class Aluno:
     
     def __init__(self, nome, ra):
        self._nome = nome
        self._ra = ra
    
     def estudar(self):
        print('Estudando')
        
     def colar (self,materia):
      print("Colando " + materia)
    
     def __str__(self):
      return "Aluno: " + self._nome + " | Ra: " + self._ra
        
     def __repr__(self):
       return "Aluno("+ self._nome + "," + self._ra + ")"
    
aluno1 = Aluno("José", "12345")
aluno2 = Aluno("Maria", " 23452")
    
print(aluno1)
print(repr(aluno2))