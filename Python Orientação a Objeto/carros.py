class Carro: 
    def __init__(self, marca, modelo, ano, cor): 
        self.cor = cor
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano 

    def exibir_informacoes(self): 
        print(f"Marca: {self.marca}") 
        print(f"Modelo: {self.modelo}") 
        print(f"Ano: {self.ano}") 
        print(f"Cor: {self.cor}")

carro1 = Carro("Toyota", "Corolla", 2020, "Prata")
carro2 = Carro("Honda", "Civic", 2019, "Preto")
carro3 = Carro("Ford", "Mustang", 2021, "Vermelho")

carro1.exibir_informacoes()
carro2.exibir_informacoes()
carro3.exibir_informacoes()