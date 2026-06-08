from modelos.restaurante import Restaurante

restaurante_praca= Restaurante("Praça", "Comida Caseira")
restaurante_mexicano = Restaurante("Mexicano", "Comida Mexicana")
restaurante_japones = Restaurante("Japonês", "Comida Japonesa")

restaurante_mexicano.alterar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()