jedi1 = ["Anakin", "Obi-Wan", "Yoda"]
print(jedi1)
print(type(jedi1))

# Criando a lista de outra forma
jedi = list(("Anakin", "Obi-Wan", "Yoda"))
print(jedi)
print(type(jedi))
#-------------------------------------------------------------------------------

# Printando um elemento especifico dentro da lista
print(jedi[-2])
print(jedi[2])

# Append vai inserir final
jedi.append("Mace Mindu")
print(jedi)

# Podemos colocar o indice onde ele vai inserir o novo elemento
jedi.insert(2, "Mace Mindu")
print(jedi)

# Append e insert com o usuário inserindo os dados
jedi.append(input("Entre com o nome do novo jedi"))
# jedi.insert(2, input("Entre com o nome do novo jedi"))

for nome in jedi:
    print(nome)

# ----------------------------------------------------------------------------------
# Apagando elementos
jedi.pop(1)
print (jedi)

jedi.remove("Yoda")
print(jedi)

#-----------------------------------------------------------------------------------
# Criação de uma lista com outra lista dentro
jedi = ["Anakin", "Obi-Wan", "Yoda", [1, 2, 6, 987]]
print(jedi)

# ----------------------------------------------------------------------------------
# Juntando duas listas com o operador matemático +
jedi = ["Anakin", "Obi-Wan", "Yoda"]
outros_jedis = ["Mace Windu", "Qui-Gon Jinn"]
todos = jedi + outros_jedis
print(todos)

# Juntando duas listas com extend
jedi.extend(outros_jedis)
print ("Jedi alterado: ")
print (jedi)

#-----------------------------------------------------------------------------------
# Metódo de copiar uma lista para outra
jedi = ["Anakin", "Obi-Wan", "Yoda"]
outros_jedis = ["Mace Windu", "Qui-Gon Jinn"]

jedi_copia = jedi.copy()
jedi_copia.append ("Rey")
print(jedi)
print (jedi_copia)

#-----------------------------------------------------------------------------------
# Descobrindo quantos elementos tem em cada lista (len)
jedi = ["Anakin", "Obi-Wan", "Yoda", "Mace Windu", "Qui-Gon Jinn", "Yoda"]
print(jedi)
print (f"Lista Original")
print(f"{jedi}")
print(f"\nTamanho da Lista: {len(jedi)}")
print(f"\nO valor Yoda aparece na Lista: {jedi.count("Yoda")} vezes")

#------------------------------------------------------------------------------------
# Invertendo ou ordenando (ordem alfabética) a lista
jedi.reverse()
print(f"\nInvertendo a lista: {jedi}")

jedi.sort()
print(f"\nOrdenando a lista: {jedi} ")

#------------------------------------------------------------------------------------
# Somando os elementos da lista
valores = [2, 3, 6, 5]
print(valores)
soma = sum(valores)
print("A soma dos elementos é {}".format(soma))

#------------------------------------------------------------------------------------
# Recortando a lista
# seq[inicio:fim:passo]
print(jedi)
print(f"Os primeiros 3 jedis {jedi[:3]}")
print(f"Os últimos 3 jedis {jedi[3:6]}")
print(f"Do segundo ao penúltimo {jedi[1:6]}")
print(f"Do segundo ao penúltimo {jedi[1:-1]}")
print(f"Somente os pares {jedi[::2]}")
print(f"Invertendo a lista {jedi[::-1]}")

#-------------------------------------------------------------------------------------
# Comando del para apagar um elemento por um índice
del jedi[-1]
print(jedi)

#Invertendo um nome com o mesmo conceito aplicado na lista
nome = "Anakin"
print(nome[::-1])

jedi = ["Anakin", "Obi-Wan", "Yoda", "Mace Windu", "Qui-Gon Jinn", "Yoda"]
print(jedi[0][::-1])