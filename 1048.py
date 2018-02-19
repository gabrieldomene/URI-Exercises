salario = float(input())

if(salario >=0 and salario <=400):
	newsalario = salario*1.15
	reajuste = salario*0.15
	percentual = '15 %'

if(salario > 400 and salario <= 800):
	newsalario = salario*1.12
	reajuste = salario*0.12
	percentual = '12 %'

if(salario > 800 and salario <= 1200):
	newsalario = salario*1.10
	reajuste = salario*0.10
	percentual = '10 %'

if(salario > 1200 and salario <= 2000):
	newsalario = salario*1.07
	reajuste = salario*0.07
	percentual = '7 %'

if(salario > 2000):
	newsalario = salario*1.04
	reajuste = salario*0.04
	percentual = "4 %"


print("Novo salario: %.2f" % newsalario)
print("Reajuste ganho: %.2f" % reajuste)
print("Em percentual:", percentual)
