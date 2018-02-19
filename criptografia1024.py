casos = int(input())
for i in range (casos):
	newstr = ""
	newstr2 = ""
	a = input()
	for word in a:
		if (word.isalpha()):
			j = ord(word) + 3
			k = chr(j)
			newstr = newstr + ''.join(k)
		else:
			newstr = newstr + ''.join(word)
	firstcripto = newstr[::-1]
	n = int(len(firstcripto)/2)
	halfone = firstcripto[0:n]
	halftwo = firstcripto[n:]

	for newword in halftwo:
		j1 = ord(newword) - 1
		k1 = chr(j1)
		newstr2 = newstr2 + ''.join(k1)
	final = halfone + newstr2
	print(final)

			
			
