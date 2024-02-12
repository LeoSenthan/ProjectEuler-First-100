total,list1=0,[]
for m in range(1,2500):
    for n in range(1,m):
        total=2*m**2+2*m*n
        list1.append(total)

found = set()
found_again = set()

for a in list1:
    if a in found_again:
        continue
    if a in found:
        found.remove(a)
        found_again.add(a)
    else:
        found.add(a)
print(len(list(found)),len(list1))
found=sorted(found)
for num in range(0,len(found)):
    if found[num]>1500000:
        print(num)
        break