# tratamento de exceções com python

try:
    idade = int(input("Por favor, insira a idade do aluno: "))
    idade_amigo = input("Por favor forneça a idade do amigo: ")

    idade_total = idade + idade_amigo
except ValueError:
    print("Por favor, entre com um valor inteiro para idade")
except TypeError:
    print("Estamos com problemas técnicos, tentando somar inteiro com string, aguarde a correção do código")
except Exception as error:
    print("Aconteceu um erro | ", error)
else:
    print("A idade do aluno é: ", idade)
    print("A idade do amigo é: ", idade_amigo)
    print("A idade total é: ", idade_total)
finally:
    print("Obrigada por usar o nosso programa!")

#ExceptionType:
# TypeError | ValueError | ZeroDivisionError | IndexError | KeyError | AttributeError
# FileNotFoundError | PermissionError | IsADirectoryError

#---------------------------------------------------------------------------------------
#criando uma classe de exceção 
# o objeto self que é o próprio da classe 
# raise 'lançar' uma exceção manualmente
    
class IdadeMaximaExcedida (Exception):
    def __str__(self):
        return "A idade não pode ser superior a 125 anos"
    
try:
    idade = int(input("Insira uma idade: "))
    if idade < 0:
        raise ValueError("O valor da idade não pode ser negativo")
    elif idade > 125:
        raise IdadeMaximaExcedida
except ValueError as error:
    print("Erro:", error)
except IdadeMaximaExcedida as error:
    print("Erro:", error)    
else:
    print(f"Você tem {idade} anos")

