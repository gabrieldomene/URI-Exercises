i = 1
while True:
	try:
		n1 = input()
		n2 = input()
		if n1 in n2:
			teste = n2.split(n1)
			qtd = len(teste)-1
			x = n2.rfind(n1)+1
			print('''Caso #{}:
Qtd.Subsequencias: {}
Pos: {}''' .format(i, qtd, x))
			i+=1	
		else:
			print("Nao contem")
	except:
		break
	