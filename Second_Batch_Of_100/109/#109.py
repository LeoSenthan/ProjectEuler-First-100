#Singles,Doubles,Triples
S = [[i,"S"+str(i)] for i in range(1,21)] + [[25,"S25"]]
D = [[i*2,"D"+str(i)] for i in range(1,21)] + [[2*25,"D25"]]
T = [[i*3,"T"+str(i)] for i in range(1,21)]

Total = D + S + T
combos = 0
for points in range(2,100): 
	for d in D:
		if d[0] < points:
			for a in Total:
				if a[0] + d[0] < points:
					for b in Total[Total.index(a):]:
						if a[0]+b[0]+d[0] == points:
							combos+=1
				elif a[0] + d[0] == points:
					combos+=1
		elif d[0] == points:
			combos+=1
print (combos)