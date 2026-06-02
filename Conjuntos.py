primeira_conjunto = {"let's data", 4, 2.1, False}

segunda_conjunto = {1,1,3,3,"repetido","repetido", "let's","let's"}
print(segunda_conjunto)  # Imprime o conjunto, mostrando apenas os elementos únicos, pois a ordem dos dados não se mantém

segunda_conjunto.add("novo elemento") # Adiciona um elemento ao conjunto'
print(segunda_conjunto)

elemento=segunda_conjunto.pop() # Remove um elemento aleatório do conjunto e o retorna
print(elemento) # Imprime o elemento removido