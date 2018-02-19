'''Dado X e Y com n digitos bits, queremos q e r tal que X = qy+r

Divisao(x,y)
Se x = 0
	entao devolva (9,9)
(q, r) = Divisao (x/2, y)
r=r*2 #deslocamento a esquerda
se x é impar
	então x = r+1
q = q*2
se r >= y
	então q = q+1, r =r-y
devolva(q, r)
'''
