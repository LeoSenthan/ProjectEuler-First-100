def check_denominator(denominator):
    while denominator % 2 == 0:
        denominator /= 2
    while denominator % 5 == 0:
        denominator /= 5
    if denominator==1:
        return True
    return False

total=0
for n in range(5,101):
    max=0
    for i in range(1,n):
        if ((n/i)**i)>max:
            max=((n/i)**i)
            if check_denominator(i**i):
                Flag=True
            else:
                Flag=False
    if Flag==True:
        print(n)
        total+=n
    elif Flag==False:
        total-=n
print(total)

    