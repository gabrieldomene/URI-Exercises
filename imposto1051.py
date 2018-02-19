sal = float(input("Salário: "))

if((sal - 4500)<0):
	imp1 = 0
else:
	imp1 = (sal-4500)*0.28
	newsal = sal - 4500

if((newsal - 3000.01)<0):
	imp2 = 0
else:
	imp2 = (newsal-3000.01)*0.18
	newsal2 = newsal - 3000.01

if((newsal2 - 2000.01)<0):
	imp3 = 0
else:
	imp3 = (newsal2-2000.01)*0.08
	newsal3 = newsal2 - 2000.01

if((newsal3 - 2000)<0):
	print("Isento")