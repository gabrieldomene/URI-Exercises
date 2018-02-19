vetor = []
for i in range(0,10):
	data_in = int(input())
	vetor.append(data_in)

for i in range (0,10):
	if vetor[i] <= 0:
		vetor[i] = 1

for i in range(0,10):
	print("X[{}] = {}" .format(i, vetor[i]))