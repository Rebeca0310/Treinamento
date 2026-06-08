class Livros:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo  # Faltava salvar o título!
        self.autor = autor
        self.ano = ano
        # Chamamos o método interno usando self
        self.disponibilidade = self.verificar_disponibilidade(ano)

    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Disponibilidade: {self.disponibilidade}"

    def emprestar(self):
        if self.disponibilidade == "Disponível":
            self.disponibilidade = "Indisponível"
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if self.disponibilidade == "Indisponível":
            self.disponibilidade = "Disponível"
            print(f"O livro '{self.titulo}' foi devolvido com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    def verificar_disponibilidade(self, ano):
        # Nota: Como você ainda está criando as instâncias, a lógica da lista 
        # (linha 30 na imagem) pode precisar de ajustes dependendo de onde 'livros_disponiveis' vem.
        # Por padrão, vamos iniciar como "Disponível" para o teste rodar:
        return "Disponível"


# Instanciando os livros (fora da classe, sem identação)
livro1 = Livros("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livros("O Alquimista", "Paulo Coelho", 1988)
livro3 = Livros("1984", "George Orwell", 1949)

print(livro1)
print(livro2)
print(livro3)   

