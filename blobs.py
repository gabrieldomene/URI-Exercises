n = int(input())
for i in range(n):
	dias = 0
	if(n <= 0):
		print(dias, "dias")
		break
	else:
		food = float(input())
		while(food > 1.0):
			food = food/2
			dias = dias + 1
		print(dias, "dias")