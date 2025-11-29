def compatible(n, m): 
    return n/10+n%10+m/10<=9 and n%10+m/10+m%10<=9
cmap = [[j for j in range(100) if compatible(i,j)] for i in range(100)]
x, y = [compatible(0,i) for i in range(100)], [0]*100
for digits in range(9):
    for i in range(100):
        for j in cmap[i]:
            y[i]+=x[j]
    x, y = y, [0]*100
print (sum(x[10:]))