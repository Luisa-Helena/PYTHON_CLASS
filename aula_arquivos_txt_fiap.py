# Abrindo um arquivo já existente
arquivo = open("C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\unwritten.txt")
print(type(arquivo))

#---------------------------------------------------------------------------------------------------------------------
# Lendo o arquivo
print(arquivo.read())

# Lendo apenas um pedaço (em bytes)
print(arquivo.read(50))

# Lendo linha a linha
for linha in arquivo.readlines():
    print(linha.restrip()) # Faz com que apenas o \n do arquivo.txt seja lido
    # print(linha, end ='') # Faz com que o final seja um espaço e não um \n

#---------------------------------------------------------------------------------------------------------------------
# Transformando em lista
linhas_do_arquivo = arquivo.readlines()
print("Ei! Eu consegui transformar meu arquivo em uma {}".format(type(linhas_do_arquivo)))
# Fechando o arquivo
arquivo.close()

# Quebrando uma linha em uma lista de palavras
linha = arquivo.readline()
palavras = linha.split()
print(palavras)

#----------------------------------------------------------------------------------------------------------------------
# Recuperando a posição do cursor
posicao = arquivo.tell()
print("Posição: ", posicao)

# Passando a posição do cursor que desejamos para que ele leia a partir disso
arquivo.seek(0)
linha = arquivo.readline()
print("Primeira linha novamente: ", linha)
# Fechando o arquivo
arquivo.close()

#--------------------------------------------------------------------------------------------------------------------
# Criando um novo arquivo 
conteudo = "Estou testando criar um arquivo de texto. Então, estou ... textando?"
arquivo = open("C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\novo_arquivo.txt", "w")
arquivo.write(conteudo)
arquivo.close()

