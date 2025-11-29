#You just need to check for one other base as n always base in base n-1
possibles=[]
for base in range(2,10**6):
    count=1+base+base**2
    power=3
    while count<10**12:
        possibles.append(count)
        count+=base**power
        power+=1
print(sum(set(possibles))+1)