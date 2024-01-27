maxlength,num=0,0
for n in range(1,1001):
    if n%2==1:
        print(n)
        multiplier=0
        while True:
            print(multiplier)
            multiplier=multiplier+1
            if ((10**multiplier)-1)%n==0:
                repeating=((10**multiplier)-1)/n
                break
        if len(str(repeating))>maxlength:
            maxlength,num=len(str(repeating)),n
print(num)