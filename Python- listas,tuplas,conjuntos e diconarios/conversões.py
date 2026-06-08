raul_seixas = ["nome", "Raul Seixas", "nascimento", "28 de junho de 1945", "falecimento", "21 de agosto de 1989", "nacionalidade", "brasileiro", "profissão", "cantor, compositor e músico" ]
print(type(raul_seixas))
raul_seixas = tuple(raul_seixas)# Converte o dicionário em uma lista
print(type(raul_seixas)) # Imprime o tipo da variável

dicionario_lets_data = dict([('DF', 'Distrito Federal'), ('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro')]) # Converte uma lista de tuplas em um dicionário
print(dicionario_lets_data) # Imprime o dicionário resultante