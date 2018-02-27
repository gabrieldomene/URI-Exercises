vetor = []

for i in range(0,100):
	data_in = float(input())
	vetor.append(data_in)
for i in range(0,100):
	if (vetor[i] <= 10):
		print("A[{}] = {:.1f}" .format(i, vetor[i]))