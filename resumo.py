import random
# importa o módulo que contém funções de aleatoriedade.
# usamos random.shuffle() para embaralhar a lista de cartas.
# import sempre fica no topo do arquivo.

class Carta:
    # Define a classe que representa UMA carta individual.
    def __init__(self, naipe, valor):
        # Método construtor: chamado quando criamos Carta(naipe, valor).
        # 'self' é a instância atual; naipe e valor são os dados da carta.
        self.naipe = naipe
        self.valor = valor
        # armazenamos naipe e valor como atributos da instância.

    def __str__(self):
        # Método especial que define a representação em string da carta.
        # É usado por print(carta) e quando transformamos a carta em str().
        return f"{self.valor} de {self.naipe}"
        # Formata, por exemplo, "A de Copas".
        # Ter __str__ facilita leitura durante testes e debug.

class Baralho:
    # Classe que representa o baralho (coleção de cartas + operações).
    def __init__(self):
        # Construtor do baralho — aqui criamos todas as cartas.
        naipes = ["Copas", "Ouros", "Espadas", "Paus"]
        # Lista com os 4 naipes tradicionais. Pode usar enums ou constantes se quiser.
        valores = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        # Lista com os valores. Para jogos específicos (ex: truco) você pode ter outros valores ou ordens.
        # Comprehension abaixo cria a combinação completa (naipe x valor).
        self.cartas = [Carta(n, v) for n in naipes for v in valores]
        # 'self.cartas' é a lista que mantém o estado atual do baralho.
        # Ao fim do __init__, o baralho tem 52 objetos Carta (4 * 13).

    def embaralhar(self):
        # Método para embaralhar as cartas do baralho.
        random.shuffle(self.cartas)
        # random.shuffle embaralha a lista in-place (modifica self.cartas).
        # Não retorna nada — apenas reorganiza a lista.

    def distribuir(self, qtd):
        # Método para distribuir 'qtd' cartas do topo do baralho.
        # Simples e eficiente: usamos slicing para pegar e remover ao mesmo tempo.
        if qtd > len(self.cartas):
            qtd = len(self.cartas)  # se pedir mais cartas do que há, devolve o que resta
            # Alternativa: lançar uma exceção em vez de ajustar qtd.
        mao = self.cartas[:qtd]
        # 'mao' recebe as primeiras 'qtd' cartas (fatia da lista).
        self.cartas = self.cartas[qtd:]
        # removemos essas cartas do baralho atual, sobrescrevendo self.cartas.
        return mao
        # devolve a lista de cartas distribuídas.

# bloco de execução: somente roda quando executamos este arquivo diretamente
if __name__ == "__main__":
    bar = Baralho()       # cria um baralho novo (52 cartas ordenadas)
    bar.embaralhar()      # embaralha as cartas
    mao1 = bar.distribuir(5)  # distribui 5 cartas (retornadas em uma lista)

    for c in mao1:        # itera sobre as cartas da mão
        print(c)          # imprime cada carta usando __str__
