vetor = []
T = int(input())
x = 0
for i in range(0,100):
	vetor.append(x)
	print("N[{}] = {}" .format(i, vetor[i]))
	if x == (T-1):
		x = 0
	else:
		x += 1