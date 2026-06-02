dicionario= {"píton": "A cobra píton (Python reticulatus) é uma das maiores cobras do mundo, podendo atingir até 7 metros de comprimento e pesar até 160 quilos. Ela é uma cobra construtora, o que significa que ela engole suas presas, e não possui veneno. A cobra é encontrada principalmente na Ásia, onde vive em florestas tropicais, rios e áreas com riachos. Embora não ataque humanos com frequência, há relatos de casos de mortes por pítons, especialmente quando se trata de pítons selvagens. A cobra é conhecida por sua habilidade de camuflagem, o que a torna difícil de ser detectada em seu habitat natural. A cobra píton é uma espécie protegida em muitos países, e a caça e o comércio ilegal de pítons são proibidos."}

dicionario={"nome": "let's data","integrantes":3}

dicionario["nome"] # Imprime o valor associado à chave "nome"
dicionario["integrantes"] # Imprime o valor associado à chave "integrantes"

dicionario.keys() # Retorna uma lista de todas as chaves do dicionário
print(dicionario.keys()) # Imprime as chaves do dicionário
dicionario.values() # Retorna uma lista de todos os valores do dicionário       
print(dicionario.values()) # Imprime os valores do dicionário
dicionario.items() # Retorna uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente       
print(dicionario.items()) # Imprime as chaves e valores do dicionário

dicionario["nome"] = "let's data 2.0" # Altera o valor associado à chave "nome"
print(dicionario) # Imprime o dicionário atualizado

raul_seixas = {"nome": "Raul Seixas", "nascimento": "28 de junho de 1945", "falecimento": "21 de agosto de 1989", "nacionalidade": "brasileiro", "profissão": "cantor, compositor e músico"}
print(type(raul_seixas))
raul_seixas = list(raul_seixas.items()) # Converte o dicionário em uma lista
print(type(raul_seixas)) # Imprime o tipo da variável
