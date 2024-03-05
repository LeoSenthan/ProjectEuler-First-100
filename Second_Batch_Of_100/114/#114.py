m, n = 3, 50
ways = [1]*3 + [0]*(48)
for k in range(3, 51):
	ways[k] = ways[k-1] + sum(ways[:k-3]) + 1
print(ways[50])
#sequence starts as [1,1,1,2]
#a(n)=2a(n-1)-a(n-2)+aa(n-4)