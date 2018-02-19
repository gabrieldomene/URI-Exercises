h1, h2 = map(int, input().split(" "))

if(h1 == h2):
	print("O JOGO DUROU 24 HORA(S)")
elif(h1 > h2):
	h2 = h2+24
	t = h2-h1
	print("O JOGO DUROU {} HORA(S)" .format(t))
else:
	t = h2-h1
	print("O JOGO DUROU {} HORA(S)" .format(t))