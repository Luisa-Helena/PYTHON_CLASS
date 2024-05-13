#c criação da função
def CalculoVelocidadeMedia(dist, temp):
    velocidade_media = dist/temp
    return "A velocidade média é {} km/h".format(velocidade_media)

#programa principal
# uso da função
distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo de viagem em horas: "))

# mensagem = CalculoVelocidadeMedia(distancia, tempo)
# print(mensagem)

print(CalculoVelocidadeMedia(distancia,tempo))

#----------------------------------------------------------------------------
#Criando a função de saudação
# o astersco faz com que o nome receba vários parâmetros
#.lower() é um metodo para garantir que a comparação seja case-insensitive

def fSaudacao(pPeriodo, *pNome):
 for i in pNome:
    if pPeriodo.lower() in ('manha', 'm'):
      print(f'Bom dia, {i}! Como vai?')
    elif pPeriodo.lower() in ('tarde', 't'):
      print(f'Boa tarde, {i}! Como vai?')
    else:
      print(f'Boa noite, {i}! Como vai?')
# #aqui começa o programa principal
fSaudacao('m','Katia')
fSaudacao('n', 'João', 'Maria', 'Pedrinho')

#-----------------------------------------------------------------------------
# Funções lembda ou inline
soma = lambda a, b: a+b
print("A soma dos valores é: ", soma(1,2))

# a primeira expressão depois dos : é se a condição for verdadeira
VerificaPositivo = lambda x: "Positivo" if x >= 0 else "Negativo"
print(VerificaPositivo(-10))

# função map
dobro = lambda x: 2*x
print(list(map(dobro, [4,5,6,8,9])))

# calculadora
def somar(a, b):
   return float(a) + float(b)
#função de subtração
def subtrair(a, b):
   return float(a) - float(b)
#função de divisão
def dividir(a, b):
   if b==0:
     return 0
   return float(a) / float(b)

#função de multiplicar
def multiplicar(a, b):
   return float(a) * float(b)