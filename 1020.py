n = int(input())
if(n>=365):
	ano = n//365
	n = (n - (ano*365))
	if(n>=30):
		mes = n//30
		n = (n - (mes*30))
		dias = n
	else:
		mes = 0
		dias = n
else:
	ano = 0
	if(n>=30):
		mes = n//30
		n = (n - (mes*30))
		dias = n
	else:
		mes = 0
		dias = n
print("%i ano(s)" % ano)
print("%i mes(es)" % mes)
print("%i dia(s)" % dias)