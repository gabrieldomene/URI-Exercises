cod, qtd = map(int, input().split(" "))

if(cod == 1):
	total = float(qtd*4)
	print("Total: R$ {0:.2f}" .format(total))
elif(cod == 2):
	total = float(qtd*4.5)
	print("Total: R$ {0:.2f}" .format(total))
elif(cod == 3):
	total = float(qtd*5)
	print("Total: R$ {0:.2f}" .format(total))
elif(cod == 4):
	total = float(qtd*2)
	print("Total: R$ {0:.2f}" .format(total))
elif(cod == 5):
	total = float(qtd*1.5)
	print("Total: R$ {0:.2f}" .format(total))