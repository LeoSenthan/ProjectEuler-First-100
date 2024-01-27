list=[]
for n in range(3,28124):
    total=0
    print(n)
    for divisor in range(1,n//2+1):
        if n%divisor==0:
            total=total+divisor
    if total>n:
        list.append(n)
newlist=[]
for num1 in list:
    for num2 in list:
        newlist.append(num1+num2)
print(sum(list(set(newlist))))