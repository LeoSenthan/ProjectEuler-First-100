#a*b=c so max length of a  is 4 and b is 4- length of a
total,digits=[],["1","2","3","4","5","6","7","8","9"]
for a in range(1000,10000):
    for b in range(2,10):
        if (sorted(str(a)+str(b)+str(a*b)))==digits:
            total.append(a*b)
for a in range(100,1000):
    for b in range(10,100):
        if (sorted(str(a)+str(b)+str(a*b)))==digits:
            total.append(a*b)
print(sum(list(set(total))))