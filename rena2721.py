r1, r2, r3, r4, r5, r6, r7, r8, r9 = map(int, input().split(" "))
total = r1+r2+r3+r4+r5+r6+r7+r8+r9
renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen"]
x = int(total/9)
for i in range(1, x+1):
	total = total - 9
if(total == 0):
	print("Rudolph")
else:
	print(renas[total-1])

