while(1):
	h1, m1, h2, m2 = map(int, input().split())
	
	if(h1 == 0 and h2 == 0 and m1 == 0  and m2 ==0):
		break;
	else:
		temp1 = (h1*60 + m1)
		temp2 = (h2*60 + m2)
		total = temp2 - temp1
		if(total < 0):
			temp2 = temp2 + 24*60
			total = temp2 - temp1
			print(total)
		else:
			print(total)
