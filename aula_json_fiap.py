# Fazendo  o import da biblioteca jason
import json

# Utilizando um dicionário como exemplo
contatos = {
    "Clark Kent":
        {"Celular":"123456",
        "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}

# Convertendo o dicionário para uma string p formato json
final = json.dumps(contatos, indent=4)

#--------------------------------------------------------------------------------------------------------------------
# Criando um arquivo
arquivo = open("C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\agenda.json", "w")

# Escrevendo o JSON dentro do arquivo
arquivo.write(final)

# Fechando o arquivo
arquivo.close()

#--------------------------------------------------------------------------------------------------------------------
# Criando uma variável de texto
conteudo = "Estou testando criar um arquivo de texto. Então, estou... textando?"

# Usando a função open para criar um objeto do tipo arquivo
arquivo = arquivo = open("C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\agenda.json", "w")

# Colocando o conteúdo do arquivo em uma variável do tipo string
conteudo_do_arquivo = arquivo.read()

# Fechando o arquivo
arquivo.close()

# Usando o método loads para converter uma string no formato json em um dicionário
agenda = json.loads(conteudo_do_arquivo)

# Comprovando que o objeto agenda é do tipo dicionário
print("O tipo do objeto agenda é {}".format(type(agenda)))