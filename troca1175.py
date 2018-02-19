vetor = []
for i in range (0,20):
	x = int(input())
	vetor.append(x)

N = vetor[::-1]
for i in range (len(N)):
	print("N[{}] = {}" .format(i, N[i]))