lista_chamada = []

N, K = map(int, input().split(" "))

for i in range(0, N):
	nome_atual = input()
	lista_chamada.append(nome_atual)

lista_chamada.sort()
print(lista_chamada[K-1])