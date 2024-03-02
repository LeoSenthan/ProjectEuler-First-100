n,t = 50,0

def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
    
for x in range(1, n+1):
    for y in range(1, n):
        m = hcfnaive(x, y)
        t += min(x*m//y, m*(n-y)//x)
print ( t*2 + n*n*3)