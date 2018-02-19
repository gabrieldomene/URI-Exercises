vetor = []
x = int(input())
vetor.append(x)
for i in range (0,9):
	vetor.append(vetor[i]*2)

for i in range(0,10):
	print("N[{}] = {}" .format(i, vetor[i]))