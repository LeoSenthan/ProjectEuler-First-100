n,lychrel=0,0
while n<10000:
    n+=1
    count,current=0,n
    while str(current)!=str(current)[::-1] or count<1:
        current+=int(str(current)[::-1])
        count+=1
        if count==50:
            lychrel+=1
            break
print(lychrel)