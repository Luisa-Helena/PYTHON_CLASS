# o usuário informa quantos alimentos consumiu naquele dia e depois informa o número de calorias de cada um dos alimentos

cal_total = 0 
qtd = 1 + (int(input("Quantos alimentos consumiu hoje? ")))
i = 0

for i in range (1,qtd):
    cal = int(input("Digite o número de calorias do alimento: "))
    cal_total = cal + cal_total 

print("A quantidade de calorias consumidas hoje é de: ",cal_total)
