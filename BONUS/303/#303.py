def f(n):
    curr=1
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
for i in range(1,101):
    total+=f(i)/i
    print(i)
print(total)
