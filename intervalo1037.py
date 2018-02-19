datain = float(input())
if((datain >= 0) and (datain <= 25)):
	print("Intervalo [0,25]")
elif((datain > 25) and (datain <= 50)):
	print("Intervalo (25,50]")
elif((datain > 50) and (datain <= 75)):
	print("Intervalo (50,75]")
elif((datain > 75) and (datain <=100)):
	print("Intervalo (75,100]")
else:
	print("Fora de intervalo")