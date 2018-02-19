casos = int(input())
for i in range(casos):
	a, b = input().split(" ")
	if b in a[-4:]:
		print("contem")
	else:
		print("nao contem")
