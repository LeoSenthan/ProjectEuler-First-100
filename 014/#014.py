maxcount,number=0,0
for n in range(2,1000000):
    start=n
    count=1
    while n!=1:
        count+=1
        if n%2==0:
            n/=2
        else:
            n=n*3+1
    if count>maxcount:
        maxcount,number=count,start
        print(start)
print(number)