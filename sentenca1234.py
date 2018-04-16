entrada = input()
saida = ""
maiuscula = True

for letra in entrada:
	if letra == " " :
		saida += " "
		continue
	if maiuscula:
		saida += letra.upper()
		maiuscula = False
	else:
		saida += letra.lower()
		maiuscula = True
print(saida)