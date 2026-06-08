primeira_lista = ["let's data", 4, 2.1, False]


print(primeira_lista[0])  # Imprime o primeiro elemento da lista
print(primeira_lista[1])  # Imprime o segundo elemento da lista
print(primeira_lista[2])  # Imprime o terceiro elemento da lista    
print(primeira_lista[3])  # Imprime o quarto elemento da lista


print(primeira_lista[-1]) # Imprime o último elemento da lista
print(primeira_lista[-2]) # Imprime o penúltimo elemento da lista       

segunda_lista = [1,1,"repetido","repetido"]
print(segunda_lista)  

lista=["1o elemento"]
lista.append("2o elemento") # Adiciona um elemento ao final da lista
print(lista)

del lista[0] # Remove o elemento na posição 0 da lista
print(lista)

lista.remove("2o elemento") # Remove o elemento "2o elemento" da lista
print(lista)

lista= ["let's", "data","4tw"]
lista[2]= "ftw" # Altera o elemento na posição 2 da lista para "ftw"
print(lista)

lista= ["let's", 'data', 'ftw']
print(len(lista)) # Retorna o número de elementos na lista

str_lets_data = "let's data"
str_lets_data_lista = list(str_lets_data) # Converte a string em uma lista de caracteres
str_lets_data_lista[6] # Tenta alterar o caractere na posição 6 da string, mas isso não é permitido em strings, pois elas são imutáveis

print(str_lets_data_lista)