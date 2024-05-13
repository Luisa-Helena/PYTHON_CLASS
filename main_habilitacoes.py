#importando o módulo que lida com as habilitacoes
import habilitacoes

habilitacoes.categorias.append("ESPECIAL")

categoria_digitada = input("Digite a categoria de habilitação: ")

habilitacoes.validar_categoria(categoria_digitada)