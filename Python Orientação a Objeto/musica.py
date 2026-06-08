class Musica:
   nome = ''
   artista = ''
   duracao =  int

musica_rock = Musica()
musica_rock.nome = "Rock in Rio"
musica_rock.artista = "Queen"
musica_rock.duracao = 300

musica_pop = Musica()
musica_pop.nome = "Shape of You"    
musica_pop.artista = "Ed Sheeran"
musica_pop.duracao = 240

def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

def listar_musicas():
    for musica in Musica.musica:
        print(f"Musica: {musica.nome}, Artista: {musica.artista}, Duração: {musica.duracao} segundos")
    
    Musica.listar_musicas()