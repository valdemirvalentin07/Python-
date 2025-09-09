class Personagem:
    def __init__(self, fraco, forte):
        self.fraco = fraco
        self.forte = forte 
        
    def luta(self):
        print(f"Luta: {self.fraco} contra {self.forte}")
        
    def empate(self):
        print(f"Empate entre {self.fraco} e {self.forte}")
        
    def __str__(self):
        return f"{self.fraco} vs {self.forte}"


class Luta:
    def __init__(self):
        self.nome_fraco = ['BrinStone','Jett','Reyna']
        self.nome_forte = ['Gekko','DeadLock','Waylay']
        
        self.combates = [   # troquei o nome para evitar conflito
            Personagem(fraco, forte)
            for fraco in self.nome_fraco 
            for forte in self.nome_forte
        ]
    
    def mostrar_batalhas(self):
        for p in self.combates:
            print(p)   # isso usa __str__ de Personagem

luta = Luta()
luta.mostrar_batalhas()
