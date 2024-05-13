# criação de uma variavel de resposta
resposta = 0
while(resposta !="42"):
    resposta = input ("Qual é a resposta para a vida, universo e tudo mais? ")

print("Parabéns! Você acertou a resposta para a vida")

# variável contadora i
# o contrário de < é o >=
i = 0

while (i <10 ):
    print("O número é: ", i)
    i = 1 + i

#------------------------------------------------------------------------------------------------
# o range sempre começa no zero
# o primeiro número é de qual número o range vai começar e o segundo é até qual número ele vai
for i in range(5,10): 
    print("O número é: ", i) 

# o parametro final é de como o range vai gerar esse número, no caso de dois em dois
for i in range(5,10, 2): 
    print("O número é: ", i) 

