n,bouncy,ratio=0,0,0
while ratio!=0.99:
    n+=1
    check=str(n)
    flaginc=True
    for char in range(0,len(check)-1):
        if int(check[char])<=int(check[char+1]):
            pass
        else:
            flaginc=False
            break
    if flaginc==False:
        flagdec=True
        for char in range(0,len(check)-1):
            if int(check[char])>=int(check[char+1]):
                pass
            else:
                flagdec=False
                break
        if flagdec==False:
            bouncy+=1
    ratio=bouncy/n
print(n)