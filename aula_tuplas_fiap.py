import sys

# Vendo o tamanho de cada variável
nome = "Bruce Wayne"
idade = 30
peso = 92.2

print("A variável nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variável idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variável peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))

# Comparando os tamanhos de uma tupla e de uma lista
lista_vazia = []
tupla_vazia = ()

print("O objeto lista vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))

#------------------------------------------------------------------------------------------------------------------------------------------
# Criando uma tupla
categorias = ("Youngling", "Padawan", "Knight", "Master")
print(categorias)

# Comando tuple
categorias = tuple(("Youngling", "Padawan", "Knight", "Master")) 
print (categorias)

print(categorias[1]) #Padawan
print(categorias[-1]) #Master

for categoria in categorias:
    print(categoria)
    
#------------------------------------------------------------------------------------------------------------------------------------------
# Identificando que é uma tupla
categorias = ("Padawan",)
print (categorias)

#------------------------------------------------------------------------------------------------------------------------------------------
# Visualizando o tamanho da tupla
categorias = ("Youngling", "Padawan", "Knight", "Master")
print(f"Tamanho da tupla {len(categorias)}")

# Não é possível fazer append ou del em tuplas pois elas são imutavéis
del categorias [-1]

#------------------------------------------------------------------------------------------------------------------------------------------
# Criando uma tupla a partir de outras tuplas
categorias_sith = ("Acolyte", "Sith Lord")
categorias_jedi = ("Youngling", "Padawan", "Knight", "Master")
categorias = categorias_jedi + categorias_sith
print(categorias)

#------------------------------------------------------------------------------------------------------------------------------------------
# Descobrindo a posição do elemento
posicao = categorias.index("Padawan")
print(posicao)

# Verificando se um elemento está ou não presente na tupla
if 'Knight' in categorias:
    print("O nível Knight está presente na tupla")