# Importando a biblioteca csv 
import csv

# Abrindo um arquivo
# arquivo_csv = open('C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\jedis.csv', 'r')
# leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')
# next(leitor_csv) #ignora a primeira linha
# for linha in leitor_csv:
#     mensagem = f"O Jedi de nome {linha[0]}, com {linha[1]} anos de idade, é classificado como {linha[2]}"
#     print(mensagem)
# arquivo_csv.close()

#------------------------------------------------------------------------------------------------------------------------------------
# Utilizando o with
# with open('C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\jedis.csv') as arquivo_csv:
#     leitor_csv = csv.reader(arquivo_csv, delimiter=',', quotechar='"')
#     next(leitor_csv) #ignora a primeira linha
#     for linha in leitor_csv:
#         mensagem = f"O Jedi de nome {linha[0]}, com {linha[1]} anos de idade, é classificado como {linha[2]}"
#         print(mensagem)

#-------------------------------------------------------------------------------------------------------------------------------------
# Inserindo dados de uma lista no arquivo 
# dados_jedi = ['Yoda', '900', 'Mestre']
# with open('C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\jedis.csv', mode ='a', newline='') as arquivo_csv:
#     escritor_csv = csv.writer(arquivo_csv, delimiter= ',')
#     escritor_csv.writerow(dados_jedi)

#-------------------------------------------------------------------------------------------------------------------------------------
# Inserindo mais de uma linha
dados_jedi = [['Yoda', '900', 'Mestre'], ['Luke Skywalker', '23', 'Padawan']]
with open('C:\\Users\\hellu\\OneDrive\\Área de Trabalho\\PYTHON_FIAP\\AULAS\\jedis.csv', mode ='a', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter= ',')
    for linha in dados_jedi:
        escritor_csv.writerow(linha)
                          