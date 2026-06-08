class Restaurante:
    nome = ''
    categoria = ''
    ativo = False



restaurante_praca= Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Comida Caseira"
restaurante_praca.ativo = False


restaurante_pizaa = Restaurante()
restaurante_pizaa.nome = "Pizzaria"
restaurante_pizaa.categoria = "Pizza"
restaurante_pizaa.ativo = False

restaurantes =[restaurante_praca, restaurante_pizaa]

print(vars(restaurante_praca))



class Restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}"
restaurante_praca= Restaurante("Praça", "Comida Caseira", False)
restaurante_pizaa = Restaurante("Pizzaria", "Pizza", False)

restaurantes =(vars(restaurante_praca), vars(restaurante_pizaa))

class Restaurante:
    restaurante = []
    def __init__(self, nome, categoria, ativo):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = ativo
        Restaurante.restaurante.append(self)
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}"
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurante:
            print(f"Restaurante: {restaurante.nome}, Categoria: {restaurante.categoria}, Ativo: {restaurante.ativo}")
            
            Restaurante.listar_restaurantes()

@classmethod
def listar_restaurantes(cls):
    print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
    for restaurante in cls.restaurantes:
        print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
@property
def ativo(self):
            return '✅' if self._ativo else '❌'
def alternar_estado(self):
    self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado() 
restaurante_pizza = Restaurante('pizza express', 'Italiana')


def listar_restaurantes():
    for restaurante in Restaurante.restaurante:
        print(f"Restaurante: {restaurante.nome .ljust(25)}, Categoria: {restaurante.categoria .ljust(25)}, Ativo: {restaurante.ativo}")
    
    Restaurante.listar_restaurantes()