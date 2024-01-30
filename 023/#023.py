list1=[]
for n in range(3,28124):
    total=0
    for divisor in range(1,n//2+2):
        if n%divisor==0:
            total+=divisor
    if total>n:
        list1.append(n)
#brute force
abundantsums,total=[],0
for num1 in range(0,len(list1)):
    for num2 in range(num1,len(list1)):
        abundantsums.append(list1[num1]+list1[num2])
abundantsums=list(set(abundantsums))
for n in range(1,28124):
    if n not in abundantsums:
        total+=n
print(total)