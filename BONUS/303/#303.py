def f(n):
    curr=1
    if list(set(str(n))) ==["9"]:
        return int("1"*len(str(n))+"2"*4*len(str(n)))
    while True:
        check=sorted(list(set(str(n*curr))))
        flag=True
        for char in check:
            if char not in "012":
                flag=False
                break
        if flag==True:
            return n*curr
        curr+=1
total=0
for i in range(1,10001):
    total+=f(i)/i
    print(i)
print(int(total))
