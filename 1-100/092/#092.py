#max value is 9*9*7=567
list=[False]
for n in range(1,568):
    while n!=89 and n!=1:
        total=0
        for digit in str(n):
            total+=int(digit)**2
        n=total
    if n==1:
        list.append(False)
    else:
        list.append(True)
for n in range(568,10000000):
    total=0
    for digit in str(n):
        total+=int(digit)**2
    list.append(True) if list[total]==True else (False)
print(list.count(True))