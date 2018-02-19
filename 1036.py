
n1, n2, n3 = input().split()
a = float(n1)
b = float(n2)
c = float(n3)
if(a == 0 or b == 0 or c == 0):
	print("Impossivel calcular")
else:
	if(((b*b) - 4*a*c) <= 0):
		print("Impossivel calcular")
	else:
		x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
		x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
		print("R1 = %.5f" % x1)
		print("R2 = %.5f" % x2)