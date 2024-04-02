val=0
def f(p, v, n): 
    global val
    tot=sum(v)
    for (i,c) in enumerate(v):
        v2=v+[]
        if c > 0:
            n2=n
            if tot==1: n2+=1
            v2[i]-=1
            for k in range(0,i):
                v2[k]+=1
            f(p*float(c)/tot,v2,n2)
    if tot == 0: val+=p*n

v=[0,0,0,0,1]
f(1,v,0)
print (round((val-2)*1000000)/1000000)