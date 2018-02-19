

n1, n2 = input().split()

if ( n2 < n1):
	dividendo = n2
	divisor = n1
else:
	dividendo = n1
	divisor = n2
dividendo = int(dividendo)
divisor = int(divisor)
c = 0
while(dividendo%divisor !=0):
	c = dividendo%divisor
	dividendo = divisor
	divisor = c

print(c)