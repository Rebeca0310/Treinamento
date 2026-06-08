class Avaliacao:
    def __init__(self, cliente, nota):
        self.cliente = cliente
        self.nota = nota
avaliacao1 = Avaliacao("João", 4.5)
avaliacao2 = Avaliacao("Maria", 3.8)
avaliacao3 = Avaliacao("Carlos", 5.0)

print(f"Avaliação de {avaliacao1.cliente}: {avaliacao1.nota}")
print(f"Avaliação de {avaliacao2.cliente}: {avaliacao2.nota}")
print(f"Avaliação de {avaliacao3.cliente}: {avaliacao3.nota}")
print(f"Média das avaliações: {media_avaliacao()}")