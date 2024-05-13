# Criando as duas listas
personagens=[]
categorias=[]

for x in range(4):
    personagens.append(input("Informe o nome do personagem: "))
    categorias.append(input("Informe a categoria do personagem: "))

for indice in range(4):
    print("O personagem {} é um(a) {}".format(personagens[indice], categorias[indice]))

#-----------------------------------------------------------------------------------------------------
# Criando um dicionário
dicionario = {}
print("O objeto dicionário é do tipo {}".format(type(dicionario)))

dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
print(dicionario)

# O primeiro elemento é chamado de chave o segundo elemento é chamado de valor ("Yoda":"Mestre Jedi")
print(dicionario["Yoda"])
print(dicionario.get("Yoda"))

# Recuperando as chaves dos dicionários
print("Chaves dicionário: ")
for chave in dicionario.keys():
    print(chave)

# Exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Incluindo um novo Jedi
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
print(dicionario)    

novo_jedi = input("Informe o nome do Jedi: ")
nova_cat_jedi = input("Informe a categoria do Jedi: ")

dicionario[novo_jedi] = nova_cat_jedi
print(dicionario)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# As chaves dentro d eum dicionário precisam ser únicas, não permite repetição
# Através da chave podemos mudar o valor para aquela chave ou através do comando update
dicionario.update({"Yoda": "SuperMestre Jedi"})
print(dicionario)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Removendo um elemento
dicionario.pop("Yoda")
print(dicionario)

# Removendo o último item
dicionario.popitem()
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

# Removendo todos os itens do dicionário
dicionario.clear()
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Criando um dicionário aninhado para a lista de contatos
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

# Esse for passará por todos os items do dicionário contatos, com a variável "contato" contendo as chaves desses items e o objeto formas contendo os valores, que são os dicionários de formas de contatos
for contato, formas in contatos.items():
    print("O contato de {} pode ser encontrado no celular {} e no email {}".format(contato, formas['Celular'], formas['Email']))