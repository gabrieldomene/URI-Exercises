#https://www.urionlinejudge.com.br/judge/pt/problems/view/1039
# entrada do raio 1 , e pts X1 Y1, entrada raio 2 e pts X2 Y2
import math
while True:
	try:
		r1, x1, y1, r2, x2, y2 = map(int, input().split())
		if(r1 < r2):
			print("MORTO")
		elif(r1>=r2):
			d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
			if(r1 >= (d+r2)):
				print("RICO")
			else:
				print("MORTO")
	except:
		break 




#calcular se r1 for maior que r2 e se a distancia euclidiana é menor que o raio do caçador