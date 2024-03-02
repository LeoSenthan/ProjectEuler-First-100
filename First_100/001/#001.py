#001
list=[]
for i in range(0,1000):
    if i%5==0 or i%3==0:
        list.append(i)
print(sum(list))