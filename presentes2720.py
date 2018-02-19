casos = int(input())
n, k = map(int, input().split(" ")) # n = presentes do papai noel, k = presente que bruninho receberá
dicionario = {}
for i in range(1, casos+2):
	cod, h, w, l = map(int, input().split(" "))
	v = h*w*l
	dicionario.update({cod:v})
print(dicionario)