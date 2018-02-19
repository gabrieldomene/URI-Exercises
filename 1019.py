time = int(input())

if(time < 60):
	h = 0
	m = 0
	s = time
	print("%i:%i:%i" %(h,m,s))
else:
	if(time <3600):
		h = 0
		m = time/60
		s = time%60
		print("%i:%i:%i" %(h,m,s))
	else:
		if(time >= 3600):
			h = time/3600
			m = (time/60)%60
			s = time%60
		print("%i:%i:%i" %(h,m,s))