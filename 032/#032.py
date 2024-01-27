#a*b=c so max length of a  is 4 and b is 4- length of a
for a in range(1,9999):
    for b in range(9999,1,-1):
        c=a*b
        string=len(set(sorted(str(a)+str(b)+str(c))))
        if len(string)==9:
            print(a,b,c)
