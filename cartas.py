import random  # biblioteca do Python

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.naipe}"


class Baralho:
    def __init__(self):
        naipes = ["Copas", "Ouros", "Espadas", "Paus"]
        valores = ["A", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "J", "Q", "K"]
        # cria todas as cartas
        self.cartas = [Carta(naipe, valor) for naipe in naipes for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, qtd):
        mao = self.cartas[:qtd]
        self.cartas = self.cartas[qtd:]  # remove as cartas já distribuídas
        return mao
    
baralho = Baralho()
baralho.embaralhar()

mao_jogador1 = baralho.distribuir(5)
mao_jogador2 = baralho.distribuir(5)

print("Jogador 1:")
for carta in mao_jogador1:
    print(carta)

print("\nJogador 2:")
for carta in mao_jogador2:
    print(carta)
